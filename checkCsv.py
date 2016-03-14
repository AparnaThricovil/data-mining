import numpy as np
import pandas as pd

inputdir = raw_input("enter directory containing the input files (C:\Users\Aparna\Anaconda\fileYearly)")
X = pd.read_csv(inputdir,header=0)
input2 = np.array(X)
#Splitting into Training and Test set
input1 = input2[:(len(input2)*4)/5]
testSet = input2[(len(input2)*4)/5:]
print input1
print "DONE\n\n"
print testSet