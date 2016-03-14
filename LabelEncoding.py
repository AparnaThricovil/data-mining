'''
@author: Aparna Gopalakrishnan
Program which would take all the attributes and convert attribute values to numeric 
'''

from sklearn import preprocessing
import pandas as pd
import csv
import os.path
import warnings

def convertlabels(inputfile,outputdir):
	#print "Inside Label Encoding\n\n"
	le = preprocessing.LabelEncoder()#Encode labels with value between 0 and n_classes-1.

	#inputFile = raw_input("enter training file")#Reads the input file with categorical attribute
	X = pd.read_csv(inputfile,header=0)

	name, ext = os.path.basename(inputfile).split(".")#Get the file name

	columnList = X.columns.values.tolist()

	directory = outputdir+'/labelled'
	if not os.path.exists(directory):
		os.makedirs(directory)

	resultFile = open(directory+'/'+name+'.csv','wb')
	wr = csv.writer(resultFile, dialect='excel')
	wr.writerow(columnList)#write the header

	attributes = []
	count = 0
	for val in columnList:
		le.fit(X[val])
		attributes.append(count)
		attributes[count] = list(le.transform(X[val]))
		count = count + 1

	rows = zip(*attributes)
	for item in rows:
		wr.writerow(item)
	return columnList
warnings.simplefilter(action = "ignore", category = FutureWarning)