import os
from pandas import read_csv
import numpy as np
import pandas as pd
from random import randint

inputdir = raw_input("enter directory containing the input files (C:\Users\Aparna\Anaconda\fileYearly)")

for file in os.listdir(inputdir):
    if file.endswith(".csv"):
        #print file
    	X = pd.read_csv(inputdir+'/'+file,header=None)
    	input2 = np.array(X)
    	
    	row_count = sum(1 for row in input2)
    	#print row_count
    	trainList = []
    	trainList.extend(range(0, row_count))
    	print trainList
    	i=0
    	testList = []
    	while(len(testList)<(row_count*0.2)):
    		k = randint(0,row_count-1)
    		if k not in testList:
    			testList.append(k)
    			trainList.remove(k)
    	print testList
    	print trainList
    	print input2[testList]
    	print input2[trainList]