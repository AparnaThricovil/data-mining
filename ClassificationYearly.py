'''
@author: Aparna Gopalakrishnan
Main Program that calls different classifiers and predicts the accuracy.
'''
import os
from pandas import read_csv
import numpy as np
import pandas as pd
import LabelEncoding
import PreProcess
import csv
import LearningCurve
import FeatureImportance
import EvaluatingClassifiers
import Split
import shutil

def removeFiles(Fpath):
    for the_file in os.listdir(Fpath):
        file_path = os.path.join(Fpath, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception, e:
            print e

inputdir = raw_input("\n\nenter directory containing the input files (C:\Users\Aparna\Anaconda\fileYearly)")
outputdir = raw_input("\n\nenter directory where output should be stored(C:\Users\Aparna\Anaconda\fileYearly\alloutputfiles)")

#Creating the labels from the categorical data to be used by classifiers.
inputfilesdir = inputdir +'/'+'inputfiles'
trainingdir = inputdir +'/'+'trainingset'
#removeFiles(trainingdir)
testlabelsdir = inputdir +'/'+'truelabels'
#removeFiles(testlabelsdir)
removeFiles(outputdir)

headers =[]

for file in os.listdir(inputfilesdir):
    if file.endswith(".csv"):
        filename = (file).split('.')
        #Split.callSplit(inputdir,filename[0])
        #print file
        #headers = LabelEncoding.convertlabels(trainingdir+'/'+file,outputdir)

for file in os.listdir(trainingdir):
    if file.endswith(".csv"):
        #print file
    	headers = LabelEncoding.convertlabels(trainingdir+'/'+file,outputdir)

labelledFilesPath = outputdir+'/labelled'
#Using one hot encoder
for file in os.listdir(labelledFilesPath):
    if file.endswith(".csv"):
    	PreProcess.convertallAttributes(labelledFilesPath+'/'+file,outputdir)

preprocessedFilesPath = outputdir+'/preprocessed'

outputfile=open(outputdir+'/ClassifiersResults.txt','a')

truelabelPath = inputdir+'/truelabels'
for file in os.listdir(labelledFilesPath):
    if file.endswith(".csv"):
    	
        filename = (file).split('.')
        #trainSet,trainSetTrueLabel = EvaluatingClassifiers.callClassifiers(preprocessedFilesPath+'/'+file,truelabelPath+'/'+file,filename[0],outputdir,inputdir,filename[1])
        trainSet,trainSetTrueLabel = EvaluatingClassifiers.callClassifiers(preprocessedFilesPath+'/'+file,truelabelPath+'/'+file,filename[0],outputdir)
        
        #LearningCurve.plotLearningCurve(trainSet, trainSetTrueLabel,outputdir+'/LearningCurve',filename[0])
        
        #FeatureImportance.findFeatures(labelledFilesPath+'/'+file,truelabelPath+'/'+file,outputdir+'/featureImportance',filename[0])
        #plotROCGraph.plotROC(X,y_true)

print "\n\nProgram Execution Complete\n"