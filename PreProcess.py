'''
@author: Aparna Gopalakrishnan
Program which would take the files with values converted to numeric and use
one-hot encoder to convert m values to m-binary features
'''
from sklearn import preprocessing
import pandas as pd
import csv
import numpy as np
import os.path
import warnings

def convertallAttributes(inputfile,outputdir):
	#print "Inside Preprocess\n\n"
	enc = preprocessing.OneHotEncoder()

	X = pd.read_csv(inputfile,header=0)

	name, ext = os.path.basename(inputfile).split(".")#Get the file name

	columnList = X.columns.values.tolist()
	
	input1 = np.array(X)

	directory = outputdir+'/preprocessed'
	if not os.path.exists(directory):#create directory in-case it does not exist.
		os.makedirs(directory)

	enc.fit(input1)

	outputlist = enc.transform(input1).toarray()
	
	resultFile = open(directory+'/'+name+'.csv','wb')
	wr = csv.writer(resultFile, dialect='excel')
	wr.writerow(columnList)#write the header

	rows = zip(*enc.transform(input1).toarray())
	
	for item in outputlist:

		wr.writerow(item)
		
warnings.simplefilter(action = "ignore", category = FutureWarning)