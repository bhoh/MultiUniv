#!/usr/bin/env python

import json
import sys
argv = sys.argv
sys.argv = argv[:1]
import ROOT
import argparse
#import optparse
import CommonPyTools.python.CommonTools as Tools
import logging
import collections
import os.path
import shutil

# Common Tools & batch
#from LatinoAnalysis.Tools.commonTools import *


# ----------------------------------------------------- DatacardFactory --------------------------------------

class DatacardFactory:
    _logger = logging.getLogger('DatacardFactory')

    # _____________________________________________________________________________
    def __init__(self):
      
        self._variables = {}
        self._cuts = {}
        self._samples = {}
        self._fileIn = None
        self._skipMissingNuisance = False

    # _____________________________________________________________________________
    # a datacard for each "cut" and each "variable" will be produced, in separate sub-folders, names after "cut/variable"
    # _____________________________________________________________________________
    def makeDatacards( self, inputFile, outputDirDatacard, variables, cuts, samples, structureFile, nuisances, groupPlot, plot):
    
        print "======================="
        print "==== makeDatacards ===="
        print "======================="
        
        self._variables = variables
        self._samples   = samples
        self._cuts      = cuts

        if os.path.isdir(inputFile):
          # ONLY COMPATIBLE WITH OUTPUTS MERGED TO SAMPLE LEVEL!!
          self._fileIn = {}
          for sampleName in self._samples:
            self._fileIn[sampleName] = ROOT.TFile.Open(inputFile+'/plots_%s_ALL_%s.root' % (self._tag, sampleName))
            if not self._fileIn[sampleName]:
              raise RuntimeError('Input file for sample ' + sampleName + ' missing')
        else:
          self._fileIn = ROOT.TFile(inputFile, "READ")

        # categorize the sample names
        signal_ids = collections.OrderedDict() # id map of alternative_signals + cumulative_signals
        alternative_signals = ['']
        cumulative_signals = []
        data = []
        background_ids = collections.OrderedDict()
        
	#print 'plot', plot
	#print 'groupPlot', groupPlot
        
        # divide the list of samples among signal, background and data
        isig = 0
        ibkg = 1
	#print self._samples
        #for sampleName in self._samples:
        for sampleName in plot:
	  if sampleName in structureFile:
            if structureFile[sampleName]['isSignal'] != 0:
              signal_ids[sampleName] = isig
              isig -= 1
            if structureFile[sampleName]['isSignal'] == 2 :
              alternative_signals.append(sampleName)
            if structureFile[sampleName]['isSignal'] == 1 :
              cumulative_signals.append(sampleName)
            if structureFile[sampleName]['isData'] == 1 :
              data.append(sampleName)
            if structureFile[sampleName]['isSignal'] == 0 and structureFile[sampleName]['isData'] == 0:
              background_ids[sampleName] = ibkg
              ibkg += 1

        for sampleName in groupPlot:
	  if sampleName in structureFile:
	    #print 'sampleName in goupPlot and structure',sampleName
            if structureFile[sampleName]['isSignal'] != 0:
              signal_ids[sampleName] = isig
              isig -= 1
            if structureFile[sampleName]['isSignal'] == 2 :
              alternative_signals.append(sampleName)
            if structureFile[sampleName]['isSignal'] == 1 :
              cumulative_signals.append(sampleName)
            if structureFile[sampleName]['isData'] == 1 :
              data.append(sampleName)
            if structureFile[sampleName]['isSignal'] == 0 and structureFile[sampleName]['isData'] == 0:
              background_ids[sampleName] = ibkg
              ibkg += 1


        print "Number of Signals:             " + str(len(signal_ids))
        print "Number of Alternative Signals: " + str(len(alternative_signals) - 1)
        print "Number of Cumulative Signals:  " + str(len(cumulative_signals))
        print "Number of Backgrounds:         " + str(len(background_ids))

        if not os.path.isdir(outputDirDatacard + "/") :
          os.mkdir(outputDirDatacard + "/")

        # loop over cuts. One directory per cut will be created
        for cutName in self._cuts:
          print "cut = ", cutName
          try:
            shutil.rmtree(outputDirDatacard + "/" + cutName)
          except OSError:
            pass
          os.mkdir(outputDirDatacard + "/" + cutName)
          
          #
          # prepare the signals and background list of samples
          # after removing the ones not to be used in this specific phase space
          #
          cut_signals = []
          cut_backgrounds = []
          for snameList, idmap in [(cut_signals, signal_ids), (cut_backgrounds, background_ids)]:
            for sampleName in idmap:
              if 'removeFromCuts' in structureFile[sampleName] and cutName in structureFile[sampleName]['removeFromCuts']:
                # remove from the list
                print ' remove ', sampleName, ' from ', cutName
              else:
                snameList.append(sampleName)

          print "  sampleNames = ", cut_signals + cut_backgrounds

          # loop over variables
          for variableName, variable in self._variables.iteritems():
            if 'cuts' in variable and cutName not in variable['cuts']:
              continue
              
            print "  variableName = ", variableName
            tagNameToAppearInDatacard = cutName
            # e.g.    hww2l2v_13TeV_of0j
            #         to be defined in cuts.py

            os.mkdir(outputDirDatacard + "/" + cutName + "/" + variableName) 
            os.mkdir(outputDirDatacard + "/" + cutName + "/" + variableName + "/shapes/") # and the folder for the root files 

            self._outFile = ROOT.TFile.Open(outputDirDatacard + "/" + cutName + "/" + variableName + "/shapes/histos_" + tagNameToAppearInDatacard + ".root", 'recreate')
                    
            # prepare yields
            yieldsSig  = {}
            yieldsBkg  = {}
            yieldsData = {}

            # Bin to be killed
            #killBinSig = {}
            #killBinBkg = {}

            for snameList, yields in [(cut_signals, yieldsSig), (cut_backgrounds, yieldsBkg), (data, yieldsData)]:
	      FlagIdx_data = 0
              for sampleName in snameList:
		if sampleName in groupPlot:
		  FlagIdx = 0
		  for subSample in groupPlot[sampleName]['samples']:
		    #print 'for',subSample,'in groupPlot'
		    if FlagIdx ==0:
		      histo = self._getHisto(cutName, variableName, subSample)
		    else:
		      histo_tmp = self._getHisto(cutName, variableName, subSample)
		      print 'adding', subSample,'to',sampleName
		      histo.Add(histo_tmp)
		    FlagIdx +=1

		  #suppress Negative
		  if groupPlot[sampleName].get('suppressNegative')==True:
		    self._fixNegativeBinAndError(histo)
		  histo.SetName('histo_%s' %(sampleName))
		else:
                  histo = self._getHisto(cutName, variableName, sampleName)
                histo.SetDirectory(self._outFile)
  
                # get the integral == rate from histogram
                if structureFile[sampleName]['isData'] == 1:
		  if FlagIdx_data == 0:
                    yields['data'] = histo.Integral()
                    histo.SetName("histo_Data")
		    FlagIdx_data += 1
		  else:
		    print 'There should be one data defined, exiting...................'
		    exit()
                else:
#                  if 'removeNegNomVal' in structureFile[sampleName] and structureFile[sampleName]['removeNegNomVal'] :
#                    for iBin in range(0,histo.GetNbinsX()+2) :
#                      BinContent = histo.GetBinContent(iBin)
#                      if BinContent < 0.1 and not BinContent == 0:
#                        print 'Killing Bin :' , sampleName , iBin , BinContent
#                        if not sampleName in killBinSig : killBinSig[sampleName] = []
#                        killBinSig[sampleName].append(iBin)
#                        histo.SetBinContent(iBin,0.)
                    
                  yields[sampleName] = histo.Integral()
  
                self._outFile.cd()
                histo.Write()

            # Loop over alternative signal samples. One card per signal (there is always at least one entry (""))
            for signalName in alternative_signals:
              if signalName == '':
                signals = [name for name in cumulative_signals if name in cut_signals]
              else:
                if signalName not in cut_signals:
                  continue
                  
                signals = [signalName] + [name for name in cumulative_signals if name in cut_signals]

              processes = signals + cut_backgrounds
             
              print "    Alternative signal: " + str(signalName)
              alternativeSignalName  = str(signalName)
              alternativeSignalTitle = ""
              if alternativeSignalName != "":
                alternativeSignalTitle = "_" + str(signalName)

              # start creating the datacard 
              cardPath = outputDirDatacard + "/" + cutName + "/" + variableName  + "/datacard" + alternativeSignalTitle + ".txt"
              print '    Writing to ' + cardPath 
              card = open( cardPath ,"w")

              print '      headers..'
              card.write('## Shape input card\n')
        
              card.write('imax * number of bins\n')
              card.write('jmax * number of processes minus 1\n')
              card.write('kmax * number of nuisance parameters\n') 
              
              card.write('-'*100+'\n')
              card.write('bin         %s' % tagNameToAppearInDatacard+'\n')
              if len(data) == 0:
                self._logger.warning( 'no data, no fun! ')
                #raise RuntimeError('No Data found!')
                yieldsData['data'] = 0

              card.write('observation %.0f\n' % yieldsData['data'])
            
              card.write('shapes  *           * '+
                         'shapes/histos_' + tagNameToAppearInDatacard + ".root" +
                         '     histo_$PROCESS histo_$PROCESS_$SYSTEMATIC' + '\n')
            
              card.write('shapes  data_obs           * '+
                         'shapes/histos_' + tagNameToAppearInDatacard + ".root" +
                         '     histo_Data' + '\n')
            
              #   shapes  *           * shapes/hww-19.36fb.mH125.of_vh2j_shape_mll.root     histo_$PROCESS histo_$PROCESS_$SYSTEMATIC
              #   shapes  data_obs    * shapes/hww-19.36fb.mH125.of_vh2j_shape_mll.root     histo_Data

              columndef = 30

              # adapt column length to long bin names            
              if len(tagNameToAppearInDatacard) >= (columndef - 5) :
                columndef = len(tagNameToAppearInDatacard) + 7

              print '      processes and rates..'
            
              card.write('bin'.ljust(40))
              card.write(''.join([tagNameToAppearInDatacard.ljust(columndef)] * (len(signals) + len(cut_backgrounds)))+'\n')
            
              card.write('process'.ljust(40))
              card.write(''.join(name.ljust(columndef) for name in signals ))
              card.write(''.join(name.ljust(columndef) for name in cut_backgrounds))
              card.write('\n')

              card.write('process'.ljust(40))
              card.write(''.join(('%d' % signal_ids[name]).ljust(columndef) for name in signals))
              card.write(''.join(('%d' % background_ids[name]).ljust(columndef) for name in cut_backgrounds))
              card.write('\n')

              card.write('rate'.ljust(40))
              card.write(''.join(('%-.4f' % yieldsSig[name]).ljust(columndef) for name in signals))
              card.write(''.join(('%-.4f' % yieldsBkg[name]).ljust(columndef) for name in cut_backgrounds))
              card.write('\n')

              card.write('-'*100+'\n')

              print '      nuisances..'

              # add normalization and shape nuisances
              for nuisanceName, nuisance in nuisances.iteritems():
                if 'type' not in nuisance:
                  raise RuntimeError('Nuisance ' + nuisanceName + ' is missing the type specification')

                if nuisanceName == 'stat' or nuisance['type'] == 'rateParam':
                  # will deal with these later
                  continue

                # check if a nuisance can be skipped because not in this particular cut
                if 'cuts' in nuisance and cutName not in nuisance['cuts']:
                    if 'sampleCuts' not in nuisance or len(set((proc, cutName) for proc in processes) & set(nuisance['samplesCuts'])) == 0:
                        continue

                if nuisance['type'] in ['lnN', 'lnU']:
                  card.write((nuisance['name']).ljust(40-20))
                  card.write((nuisance['type']).ljust(20))
                  if 'all' in nuisance and nuisance ['all'] == 1: # for all samples
                    card.write(''.join(('%-.4f' % nuisance['value']).ljust(columndef) for _ in processes))
                  else:
                    # apply only to selected samples
                    for sampleName in processes:
                      if sampleName in nuisance['samples'] or ('samplesCuts' in nuisance and (sampleName, cutName) in nuisance['samplesCuts']):
                        # in this case nuisance['samples'] is a dict mapping sample name to nuisance values in string
                        card.write(('%s' % nuisance['samples'][sampleName]).ljust(columndef))
                      else:
                        card.write(('-').ljust(columndef))
                
                elif nuisance['type'] == 'shape':
                  #
                  # 'skipCMS' is a flag not to introduce "CMS" automatically in the name
                  #      of the nuisance.
                  #      It may be needed for combination purposes with ATLAS
                  #      and agreed upon for all CMS analyses.
                  #      For example: theoretical uncertainties on ggH with migration scheme 2017
                  #
                  if 'skipCMS' in nuisance and nuisance['skipCMS'] == 1:
                    card.write(nuisance['name'].ljust(40-20))
                  else:
                    card.write(("CMS_" + nuisance['name']).ljust(40-20))

                  if 'AsLnN' in nuisance and float(nuisance['AsLnN']) >= 1.:
                    print ">>>>>", nuisance['name'], " was derived as a shape uncertainty but is being treated as a lnN"
                    card.write(('lnN').ljust(20))
                    for sampleName in processes:
                      if ('all' in nuisance and nuisance['all'] == 1) or \
                              ('samples' in nuisance and sampleName in nuisance['samples']) or \
                              ('samplesCuts' in nuisance and (sampleName, cutName) in nuisance['samplesCuts']):
			if sampleName in groupPlot:
			  subIdx = 0
			  for subSample in groupPlot[sampleName]['samples']:
			    if subIdx == 0:
                              histo = self._getHisto(cutName, variableName, subSample)
                              histoUp = self._getHisto(cutName, variableName, subSample, '_' + nuisance['name'] + 'Up') 
                              histoDown = self._getHisto(cutName, variableName, subSample, '_' + nuisance['name'] + 'Down')
			    else:
                              histo_tmp = self._getHisto(cutName, variableName, subSample)
                              histoUp_tmp = self._getHisto(cutName, variableName, subSample, '_' + nuisance['name'] + 'Up') 
                              histoDown_tmp = self._getHisto(cutName, variableName, subSample, '_' + nuisance['name'] + 'Down')
                              histo.Add(histo_tmp)
			      histoUp.Add(histoUp_tmp)
                              histoDown.Add(histoDown_tmp)
			    subIdx += 1
                          histo.SetName('histo_%s' %(sampleName))
                          histoUp.SetName('histo_%s' %(sampleName+'_'+nuisance['name']+'Up')) 
                          histoDown.SetName('histo_%s' %(sampleName+'_'+nuisance['name']+'Down'))
			else:
                          histo = self._getHisto(cutName, variableName, sampleName)
                          histoUp = self._getHisto(cutName, variableName, sampleName, '_' + nuisance['name'] + 'Up') 
                          histoDown = self._getHisto(cutName, variableName, sampleName, '_' + nuisance['name'] + 'Down')

                        if (not histoUp or not histoDown):
                          print '########################################################################'
                          print 'Histogram for nuisance', nuisance['name'], 'on sample', sampleName, 'missing'
                          print '########################################################################'

                          if self._skipMissingNuisance:
                            card.write(('-').ljust(columndef)) 
                            continue
			  else:
			    print 'Exiting....................................'
			    exit()

                        histoIntegral = histo.Integral()
                        histoUpIntegral = histoUp.Integral()
                        histoDownIntegral = histoDown.Integral()
                        if histoIntegral > 0. and histoUpIntegral > 0.:
                          diffUp = (histoUpIntegral - histoIntegral)/histoIntegral/float(nuisance['AsLnN'])
                        else: 
                          diffUp = 0.

                        if histoIntegral > 0. and histoDownIntegral > 0.:
                          diffDo = (histoDownIntegral - histoIntegral)/histoIntegral/float(nuisance['AsLnN'])
                        else:
                          diffDo = 0.

                        if 'symmetrize' in nuisance and nuisance['symmetrize']:
                          diff = (diffUp - diffDo) * 0.5
                          if diff >= 1.:
                              # can't symmetrize
                              diffUp = diff * 2. - 0.999
                              diffDo = -0.999
                          elif diff <= -1.:
                              diffUp = -0.999
                              diffDo = -diff * 2. - 0.999
                          else:
                              diffUp = diff
                              diffDo = -diff
        
                        lnNUp = 1. + diffUp
                        lnNDo = 1. + diffDo

                        #  
                        # avoid 0.00/XXX and XXX/0.00 in the lnN --> ill defined nuisance
                        # if this happens put 0.00 ---> 1.00, meaning *no* effect of this nuisance
                        #              Done like this because it is very likely what you are experiencing 
                        #              is a MC fluctuation in the varied sample, that is the up/down histogram has 0 entries!
                        #
                        #              NB: with the requirement "histoUpIntegral > 0" and "histoDownIntegral > 0" this should never happen, 
                        #                  except for some strange coincidence of "AsLnN" ... 
                        #                  This fix is left, just for sake of safety
                        #
                        if lnNUp==0: lnNUp = 1
                        if lnNDo==0: lnNDo = 1
            
                        card.write((('%-.4f' % lnNUp)+"/"+('%-.4f' % lnNDo)).ljust(columndef))
                      else:
                        card.write(('-').ljust(columndef)) 

                  else:  
                    card.write('shape'.ljust(20))
                    for sampleName in processes:
                      if ('all' in nuisance and nuisance ['all'] == 1) or \
                              ('samples' in nuisance and sampleName in nuisance['samples']) or \
                              ('samplesCuts' in nuisance and (sampleName, cutName) in nuisance['samplesCuts']):
                        # save the nuisance histograms in the root file
                        if ('skipCMS' in nuisance.keys()) and nuisance['skipCMS'] == 1:
                          suffixOut = None
                        else:
                          suffixOut = '_CMS_' + nuisance['name']

                        symmetrize = 'symmetrize' in nuisance and nuisance['symmetrize']

                        saved = self._saveNuisanceHistos(cutName, variableName, sampleName, '_' + nuisance['name'], suffixOut, symmetrize)
                        if saved:
                          card.write('1.000'.ljust(columndef))
                        else:
                          # saved can be false if skipMissingNuisance is true and histogram cannot be found
                          card.write(('-').ljust(columndef))
                      else:
                        card.write(('-').ljust(columndef))

                card.write('\n')
                
              # done with normalization and shape nuisances.
              # now add the stat nuisances
              if 'stat' in nuisances:
                nuisance = nuisances['stat']
                
                if nuisance['type'] == 'auto':
                  # use autoMCStats feature of combine
                  card.write('* autoMCStats ' + nuisance['maxPoiss'] + '  ' + nuisance['includeSignal'])
                  #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
                  #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
                  card.write('\n')

                else:
                  # otherwise we process stat nuisances sample-by-sample
                  for sampleName in processes:
                    if sampleName not in nuisance['samples']:
                      continue
  
                    sampleNuisance = nuisance['samples'][sampleName]
                    sampleIndex = processes.index(sampleName)
  
                    if sampleNuisance['typeStat'] == 'uni' : # unified approach
                      # save the nuisance histograms in the root file
                      saved = self._saveNuisanceHistos(cutName, variableName, sampleName, 'stat', '_CMS_' + tagNameToAppearInDatacard + "_" + sampleName + "_stat")
  
                      if saved:
                        card.write(('CMS_' + tagNameToAppearInDatacard + "_" + sampleName + "_stat").ljust(40-20))
                        card.write((nuisance['type']).ljust(20))
    
                        # write the line in datacard. Only the column for this sample gets 1.000
                        for idx in range(len(processes)):
                          if idx == sampleIndex:
                            card.write(('1.000').ljust(columndef))
                          else:
                            card.write(('-').ljust(columndef))
    
                        card.write('\n')
  
                    elif sampleNuisance['typeStat'] == 'bbb': # bin-by-bin
                      histoTemplate = self._getHisto(cutName, variableName, sampleName)
                      for iBin in range(1, histoTemplate.GetNbinsX()+1):
                        if 'correlate' in sampleNuisance:
                          #specify the sample that is source of the variation
                          tag = "_ibin"+sampleName+"_"
                          correlate = list(sampleNuisance["correlate"]) # list of sample names to correlate bin-by-bin with this sample
                        else:
                          tag = "_ibin_"
                          correlate = []
  
                        # save the nuisance histograms in the root file
                        saved = self._saveNuisanceHistos(cutName, variableName, sampleName, tag + str(iBin) + '_stat',
                            '_CMS_' + tagNameToAppearInDatacard + "_" + sampleName + '_ibin_' + str(iBin) + '_stat')
  
                        if not saved:
                          continue
  
                        for other in list(correlate):
                          saved = self._saveNuisanceHistos(cutName, variableName, other, tag + str(iBin) + '_stat',
                              '_CMS_' + tagNameToAppearInDatacard + "_" + sampleName + '_ibin_' + str(iBin) + '_stat')
                          if not saved:
                            correlate.remove(other)
  
                        card.write(('CMS_' + tagNameToAppearInDatacard + "_" + sampleName + "_ibin_" + str(iBin) + "_stat").ljust(100-20))
                        card.write((nuisance['type']).ljust(20))
  
                        # write line in datacard. One line per sample per bin
                        for idx in range(len(processes)):
                          if idx == sampleIndex or processes[idx] in correlate:
                            card.write(('1.000').ljust(columndef))
                          else:
                            card.write(('-').ljust(columndef))
                      
                        card.write('\n')

              # now add the "rateParam" for the normalization
              #  e.g.:            z_norm rateParam  htsearch zll 1 
              # see: https://twiki.cern.ch/twiki/bin/view/CMS/HiggsWG/SWGuideNonStandardCombineUses#Rate_Parameters
              # 'rateParam' has a separate treatment -> it's just a line at the end of the datacard. It defines "free floating" samples
              # I do it here and not before because I want the freee floating parameters at the end of the datacard
              for nuisance in nuisances.itervalues():
                if nuisance['type'] != 'rateParam':
                  continue

                # check if a nuisance can be skipped because not in this particular cut
                if 'cuts' in nuisance and cutName not in nuisance['cuts']:
                  continue

                card.write(nuisance['name'].ljust(40-20))
                card.write('rateParam'.ljust(20))
                card.write(tagNameToAppearInDatacard.ljust(columndef))   # the bin
                # there can be only 1 sample per rateParam
                if len(nuisance['samples']) != 1:
                  raise RuntimeError('Invalid rateParam: number of samples != 1')

                sampleName, initialValue = nuisance['samples'].items()[0]
                if sampleName not in self._samples and sampleName not in groupPlot:
                  raise RuntimeError('Invalid rateParam: unknown sample %s' % sampleName)

                card.write(sampleName.ljust(20))
                card.write(('%-.4f' % float(initialValue)).ljust(columndef))
                card.write('\n')

              # now add other nuisances            
              # Are there other kind of nuisances I forgot?
            
              card.write('-'*100+'\n')

              card.write('\n')
              card.close()

              print '      done.'

            self._outFile.Close()

        if type(self._fileIn) is dict:
          for source in self._fileIn.values():
            source.Close()
        else:
          self._fileIn.Close()


    # _____________________________________________________________________________
    def _saveNuisanceHistos(self, cutName, variableName, sampleName, suffixIn, suffixOut = None, symmetrize = False):
        if sampleName in groupPlot:
	  subIdx = 0
	  for subSample in groupPlot[sampleName]['samples']:
	    if subIdx == 0:
	      histo = self._getHisto(cutName, variableName, subSample)
              histoUp = self._getHisto(cutName, variableName, subSample, suffixIn + 'Up')
              histoDown = self._getHisto(cutName, variableName, subSample, suffixIn + 'Down')
	      if not histoUp:
	        print("WARNING: histoUp is null object, instead use histo")
	        histoUp =  histo.Clone()
	      if not histoDown:
		print("WARNING: histoDown is null object, instead use histo")
	        histoDown = histo.Clone()
	    else:
              histo_tmp = self._getHisto(cutName, variableName, subSample)
              histoUp_tmp = self._getHisto(cutName, variableName, subSample, suffixIn + 'Up')
              histoDown_tmp = self._getHisto(cutName, variableName, subSample, suffixIn + 'Down')
	      if histoUp_tmp:
	        histoUp.Add(histoUp_tmp)
	      else:
	        print("WARNING: histoUp_tmp is null object, instead add histo_tmp")
		histoUp.Add(histo_tmp)
	      if histoDown_tmp:
                histoDown.Add(histoDown_tmp)
	      else:
		print("WARNING: histoDown_tmp is null object, instead add histo_tmp")
		histoDown.Add(histo_tmp)
	    subIdx += 1
	  histoUp.SetName('histo_%s' %(sampleName+suffixIn+'Up'))
	  histoDown.SetName('histo_%s' %(sampleName+suffixIn+'Down'))
	else:
          histoUp = self._getHisto(cutName, variableName, sampleName, suffixIn + 'Up')
          histoDown = self._getHisto(cutName, variableName, sampleName, suffixIn + 'Down')

        if not histoUp or not histoDown:
          print 'Up/down histogram for', cutName, variableName, sampleName, suffixIn, 'missing'
          if self._skipMissingNuisance:
            return False
          # else let ROOT raise

        if symmetrize:
	  if sampleName in groupPlot:
	    subIdx = 0
	    for subSample in groupPlot[sampleName]['samples']:
	      if subIdx == 0:
                histoNom = self._getHisto(cutName, variableName, subSample)
	      else:
                histoNom_tmp = self._getHisto(cutName, variableName, subSample)
		histoNom.Add(histoNom_tmp)
	      subIdx += 1
	    histoNom.SetName('histo_%s' %(sampleName))
	  else:
            histoNom = self._getHisto(cutName, variableName, sampleName)
          histoDiff = histoUp.Clone('histoDiff')
          histoDiff.Add(histoDown, -1.)
          histoDiff.Scale(0.5)
          histoUp.Reset()
          histoUp.Add(histoNom)
          histoUp.Add(histoDiff)
          histoDown.Reset()
          histoDown.Add(histoNom)
          histoDown.Add(histoDiff, -1.)

        histoUp.SetDirectory(self._outFile)
        histoDown.SetDirectory(self._outFile)
        if suffixOut:
            histoUp.SetName('histo_%s%sUp' % (sampleName, suffixOut))
            histoDown.SetName('histo_%s%sDown' % (sampleName, suffixOut))

        self._outFile.cd()
        histoUp.Write()
        histoDown.Write()

        return True

    # _____________________________________________________________________________
    def _getHisto(self, cutName, variableName, sampleName, suffix = None):
        shapeName = '%s/%s/histo_%s' % (cutName, variableName, sampleName)
        if suffix:
            shapeName += suffix
	
	print 'getting histo',shapeName

        if type(self._fileIn) is dict:
            # by-sample ROOT file
            histo = self._fileIn[sampleName].Get(shapeName)
        else:
            # Merged single ROOT file
            histo = self._fileIn.Get(shapeName)
      
        return histo

    def _fixNegativeBinAndError(self, histogram_to_be_fixed):
        # if a histogram has a bin < 0
        # then put the bin content to 0
        # and also if a histogram has uncertainties that go <0,
        # then put the uncertainty to the maximum allowed
  
        for ibin in range(1, histogram_to_be_fixed.GetNbinsX()+1) :
            if histogram_to_be_fixed.GetBinContent(ibin) < 0 :
  	        histogram_to_be_fixed.SetBinContent(ibin, 0) 
  
        # the SetBinError does not allow asymmetric -> fine, maximum uncertainty set
        for ibin in range(1, histogram_to_be_fixed.GetNbinsX()+1) :
            if histogram_to_be_fixed.GetBinContent(ibin) - histogram_to_be_fixed.GetBinErrorLow(ibin) < 0 :
  	        histogram_to_be_fixed.SetBinError(ibin, histogram_to_be_fixed.GetBinContent(ibin)) 
  
  

if __name__ == '__main__':
    sys.argv = argv
    
    print '''
--------------------------------------------------------------------------------------------------

  __ \          |                                 |       \  |         |                
  |   |   _` |  __|   _` |   __|   _` |   __|  _` |      |\/ |   _` |  |  /   _ \   __| 
  |   |  (   |  |    (   |  (     (   |  |    (   |      |   |  (   |    <    __/  |    
 ____/  \__,_| \__| \__,_| \___| \__,_| _|   \__,_|     _|  _| \__,_| _|\_\ \___| _|    
                                                                                
--------------------------------------------------------------------------------------------------
'''    

    parser = argparse.ArgumentParser(description='Joker')
    parser.add_argument('--userflags', dest='Userflags', default="test")
    parser.add_argument('--sigset'             , dest='sigset'            , help='Signal samples [SM]'                        , default='SM')
    parser.add_argument('--outputDirDatacard'  , dest='outputDirDatacard' , help='output directory'                           , default='./')
    parser.add_argument('--inputFile'          , dest='inputFile'         , help='input directory'                            , default='./input.root')
    parser.add_argument('--cardList'           , dest="cardList"          , help="List of cuts to produce datacards"          , default=[])
    parser.add_argument('--skipMissingNuisance', dest='skipMissingNuisance', help="Don't write nuisance lines when histograms are missing", default=False, action='store_true')
        

    ROOT.gROOT.SetBatch()
    ROOT.TH1.SetDefaultSumw2(True)

    # read default parsing options as well
    Tools.AddOptions(parser)
    Tools.LoadOptDefaults(parser)
    opt = parser.parse_args()

    sys.argv.append( '-b' )


 
    if not opt.debug:
        pass
    elif opt.debug == 2:
        print 'Logging level set to DEBUG (%d)' % opt.debug
        logging.basicConfig( level=logging.DEBUG )
    elif opt.debug == 1:
        print 'Logging level set to INFO (%d)' % opt.debug
        logging.basicConfig( level=logging.INFO )

    Userflags = []
    if opt.Userflags != "":
      Userflags = (opt.Userflags).split(',')
    
    IsFirstFlag = True
    tag=''
    for flag in Userflags:
      if IsFirstFlag:
        tag = flag
      else:
        tag += '_'+flag 
    print tag

    if opt.outputDirDatacard == "./":
      opt.outputDirDatacard = 'DataCard_'+tag
    else:
      opt.outputDirDatacard = opt.outputDirDatacard + '_' + tag

    print " configuration file = 	", opt.pycfg
    print " inputFile =                 ", opt.inputFile
    print " outputDirDatacard =         ", opt.outputDirDatacard
    print " cardList:			", opt.cardList
      
    factory = DatacardFactory()
    factory._tag       = tag
    factory._skipMissingNuisance = opt.skipMissingNuisance
    
    # ~~~~
    samples = {}
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()
   
    cuts = {}
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()

    variables = {}
    if os.path.exists(opt.variablesFile) :
      handle = open(opt.variablesFile,'r')
      exec(handle)
      handle.close()
      
    if len(opt.cardList)>0:
      try:
        newCuts = []
        for iCut in opt.cardList:
          for iOptim in optim:
            newCuts.append(iCut+'_'+iOptim)
        opt.cardList = newCuts
        print opt.cardList
      except:
        print "No optim dictionary"
      cut2del = []
      for iCut in cuts:
        if not iCut in opt.cardList : cut2del.append(iCut)
      for iCut in cut2del : del cuts[iCut]   
  

    # ~~~~
    structure = collections.OrderedDict()
    if opt.structureFile == None :
       print " Please provide the datacard structure "
       exit ()
       
    if os.path.exists(opt.structureFile) :
      handle = open(opt.structureFile,'r')
      exec(handle)
      handle.close()

    groupPlot = collections.OrderedDict()
    plot = {}
    legend = {}
    if os.path.exists(opt.plotFile) :
      handle = open(opt.plotFile,'r')
      exec(handle)
      handle.close()

    # ~~~~
    nuisances = collections.OrderedDict()
    if opt.nuisancesFile == None :
       print " Please provide the nuisances structure if you want to add nuisances "
       
    if os.path.exists(opt.nuisancesFile) :
      handle = open(opt.nuisancesFile,'r')
      exec(handle)
      handle.close()
    

    factory.makeDatacards( opt.inputFile ,opt.outputDirDatacard, variables, cuts, samples, structure, nuisances, groupPlot, plot)

