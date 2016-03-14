import re
import pandas as pd
import numpy as np
import os
#First Input is the text file
inputdir = raw_input("enter directory containing the input files (C:\Users\Aparna\Anaconda\SearchStudents)")
#file = open('list.txt', 'r')

X = pd.read_csv(inputdir+"/grad.csv",header=0)
input1 = np.array(X)
for row in input1:
	print row
