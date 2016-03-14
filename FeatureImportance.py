'''
@author: Aparna Gopalakrishnan
Program that calculates the chi2 value with and without considering p-values
'''
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_selection import chi2
import os

def findFeatures(X,y,fileStorePath,fileName):

  print "Inside finding important features for the "+fileName+" data set"

  inputFile = pd.read_csv(X,header=0)
  input1 = np.array(inputFile)
  
  label = pd.read_csv(y,header=0)
  Y = np.array(label)
  chiVal,pVal = chi2(input1, Y)#Calculate the chi2 value

  indices = chiVal
  chi2List = []
  chi2Index = []

  for i, val in enumerate(pVal):
    if val<0.05:
      chi2List.append(chiVal[i])
      chi2Index.append(i)

  print chi2Index

  i=0
  if(fileName == "cad" or fileName == "health" or fileName == "science"):
    i=12
  elif(fileName == "grade"):
    i=16
  elif(fileName == "graduated"):
    i=14
  else:
    i=13
  if not os.path.exists(fileStorePath):
    os.makedirs(fileStorePath)
  if not os.path.exists(fileStorePath+'/FeatureImportancewith-P-value/'):
    os.makedirs(fileStorePath+'/FeatureImportancewith-P-value/')
  # Plot the feature importances of the forest
  plt.figure()
  plt.title("Feature importance - chi2 analysis")
  plt.bar(range(i), indices,
         color="r", align="center")
  plt.xticks(range(i))
  plt.xlim([-1, i])
  plt.ylabel('chi2 value')
  plt.xlabel('Features numbered(0 through %d)' % (i-1))
  plt.savefig(fileStorePath+'/'+fileName+'.png')
  plt.close()
  plt.clf()#clear the figure for next loop

  #Plot figures with p-values
  plt.figure()
  plt.title("chi2 analysis considering features with p-value less than 0.05")
  plt.bar(chi2Index, chi2List,
         color="r", align="center")
  plt.xticks(chi2Index)
  plt.xlim([-1, i])
  plt.ylabel('chi2 value')
  plt.xlabel('Onl;y relevant features displayed')
  plt.savefig(fileStorePath+'/FeatureImportancewith-P-value/'+fileName+'.png')
  plt.close()
  plt.clf()#clear the figure for next loop