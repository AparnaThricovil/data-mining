'''
Created on August 24, 2015

@author: Aparna
'''
'''
This program find the prior and conditional probability 
for all the attributes
'''

import csv
import sys
reload(sys)
import re
import nltk
import math

def getProbabilities(inputfilelocation,outputFileLocation):
    print "Inside Naive Bayes program"
    inputfile = inputfilelocation
    text = open(inputfile,'rb')
    csvFileRead = csv.reader(text) #Read the csv input file
    totalDataSet = 0 #to count the number of data set rows
    classLabelDictionary = {} # this dictionary will hold the probability of occurrence of the class labels
    classLabelwithAttributeDict = {}
    newlist=[]
    headerRow = []
    for row in csvFileRead:
        if totalDataSet==0:
            headerRow = row
            totalDataSet+=1
            print headerRow
            continue
        else:
            totalDataSet+=1
            mylist=list(row)
            newlist = mylist[0:len(mylist)-1]
            #Assumption that the class label is the last attribute
            keyClassLabel = mylist[-1] #get the class label
            '''
            If the class label was found earlier then increment the value 
            for the class label key. But if class label is not found as a 
            key in the dictionary then add the class label as a new key and
            set the value as 1.
            '''
            if keyClassLabel in classLabelDictionary:
                classLabelDictionary[keyClassLabel]+=1
            else:
                classLabelDictionary[keyClassLabel]=1
                classLabelwithAttributeDict[keyClassLabel]={}
                #print classLabelwithAttributeDict
                #print classLabelDictionary
    #Find the probability of occurrence of class label    
    for key in classLabelDictionary:
        classLabelDictionary[key]=classLabelDictionary[key]/float(totalDataSet-1)
        i=0;
        while i<len(newlist):
            classLabelwithAttributeDict[key][headerRow[i]]={}
            
            i+=1
    #print classLabelwithAttributeDict
    text = open(inputfile,'rb')
    csvFileRead = csv.reader(text)
    totalDataSet =0
    for row in csvFileRead:
        #print "here"
        if totalDataSet==0:#don't consider header row
            totalDataSet+=1
            continue
        else:
            totalDataSet+=1
            mylist=list(row)
            #print len(mylist)
            newlist = mylist[0:len(mylist)-1]
            
            #Assumption that the class label is the last attribute
            keyClassLabel = mylist[-1] #get the class label
            #print keyClassLabel
            i=0
            
            for attribute in newlist:

                if attribute in classLabelwithAttributeDict[keyClassLabel][headerRow[i]]:
                    classLabelwithAttributeDict[keyClassLabel][headerRow[i]][attribute]+=1
                else:
                    classLabelwithAttributeDict[keyClassLabel][headerRow[i]][attribute]=1
                i+=1
    
    #find the conditional probabilities
    for masterkey in classLabelwithAttributeDict:
        for childkey in classLabelwithAttributeDict[masterkey]:
            sumPerAttribute = float(sum(classLabelwithAttributeDict[masterkey][childkey].values()))
            for leafkey in classLabelwithAttributeDict[masterkey][childkey]:
                #print classLabelwithAttributeDict[masterkey][childkey][leafkey]
                classLabelwithAttributeDict[masterkey][childkey][leafkey]/=sumPerAttribute
                classLabelwithAttributeDict[masterkey][childkey][leafkey] = round(classLabelwithAttributeDict[masterkey][childkey][leafkey],2)
#writing the probabilities into csv
    
    writer = csv.writer(open(outputFileLocation+'/Conditional probabilities.csv', 'wb'))
    
    for key, value in classLabelwithAttributeDict.iteritems():
        writer.writerow([key, value])
    for key, value in classLabelDictionary.iteritems():
        writer.writerow([key, value])

    return classLabelDictionary, classLabelwithAttributeDict
'''if __name__ == "__main__":
    getProbabilities()'''