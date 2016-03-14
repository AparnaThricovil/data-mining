'''
Created on August 24th, 2015

@author: Aparna
'''
'''
This program is to calculate the conditional probabilities.

The input to this program is the csv file with the first row containing all the attributes names
The output file finally will contain the results
'''
##############################
#INPUT 
#######Input file - Data set file with both test and training data.
					#csv format Example: C:/Users/Aparna/Anaconda/input.csv
#######Output file location - Location where the final files should be created.
#######K - the value of k for k-fold validation
##############################

from pandas import read_csv
import pandas as pd
import numpy as np
import os
import GetProbability

#input the file
inputFile = raw_input("Please enter the location of the input file(file name should be in this format: C:/Users/Aparna/Anaconda/Input.csv)")

#input the output file location
print "\n"
outputFileLocation = raw_input("Please enter the location for the output files")

priorProbDict, condProbDict = GetProbability.getProbabilities(inputFile,outputFileLocation)# call naive Bayesian

#print condProbDict
print "\n\nComplete"
print "\n\nOutput in FinalResults.txt file\n\n"