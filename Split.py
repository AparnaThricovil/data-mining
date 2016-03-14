'''
@author: Aparna Gopalakrishnan
Main Program that calls different classifiers and predicts the accuracy.
'''
import os
from pandas import read_csv
import numpy as np
import pandas as pd
import csv


def callSplit(inputdir,filename):
	#inputdir = raw_input("\n\nenter directory containing the input files (C:\Users\Aparna\Anaconda\fileYearly)")

	#Creating the labels from the categorical data to be used by classifiers.
	inputfilesdir = inputdir +'/'+'inputfiles'
	trainingdir = inputdir +'/'+'trainingset'
	testlabelsdir = inputdir +'/'+'truelabels'
	headers =[]
	for file in os.listdir(inputfilesdir):
	    if file.endswith(".csv"):
	        #print file
	    	#headers = LabelEncoding.convertlabels(trainingdir+'/'+file,outputdir)
	    	X = pd.read_csv(inputfilesdir+'/'+file,header=0)
	    	columnList = X.columns.values.tolist()
	    	
	    	labelFile = open(testlabelsdir+'/testlabel'+'.csv','wb')
	    	X[columnList].to_csv(labelFile)
	    	#print X[columnList[0]]
	    	
	    	labelFile.close()
	    	labelFile = testlabelsdir+'/testlabel'+'.csv'
	    	outlabel = testlabelsdir+'/'+filename+'.csv'
	    	headerRow=True
	    	itemList=[]
	    	with open(labelFile,'r') as fin:
	    		with open(outlabel,'wb') as fout:
	    			writer=csv.writer(fout)
	    			for row in csv.reader(fin):
	    				itemList=row
	    				#print itemList[-1]
	    				#writer.writerow(row[-1:])Not Graduated
	    				if (headerRow):
	    					writer.writerow(['Class Label'])
	    					headerRow = False
	    				elif 'Not Persisted' in itemList[-1] or 'Not Graduated' in itemList[-1]:
	    					writer.writerow([0])
	    				else:
	    					writer.writerow([1])
	    	os.remove(labelFile)

	    	columnList.remove(columnList[-1])

	    	resultFile = open(trainingdir+'/test'+'.csv','wb')
	    	outname = trainingdir+'/'+filename+'.csv'
	    	X[columnList].to_csv(resultFile)
	    	resultFile.close()

	    	resultFile = trainingdir+'/test'+'.csv'
	    	with open(resultFile,'r') as fin:
	    		with open(outname,'wb') as fout:
	    			writer=csv.writer(fout)
	    			for row in csv.reader(fin):
	    				writer.writerow(row[1:])
	    	
	    	os.remove(resultFile)
	return