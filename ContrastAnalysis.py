'''
Created on September 3rd, 2015

@author: Aparna
'''
'''
This program is to read the text file containing closed frequent item sets generated by 
Christian Borgelt's Apriori implementation and to remove the item sets that does not 
contain the class label. 

The input to this program is a text file with each row containing a closed item set.
The output file is also a text file with only closed item sets that has the class label.
'''
from pandas import read_csv
import pandas as pd
import numpy as np
import os
import re
from collections import defaultdict
import csv
import math
import chi2Calculation

def findmax(listItems):
    maxSup=0
    for items in listItems:
        originalFile.seek(0)
        itemCount = 0
        for row in csv_f:
            if items in row:
                itemCount = itemCount + 1
            if(itemCount>maxSup):
                maxSup = itemCount
    return maxSup
#input the file
inputdir = raw_input("Please enter the location of the input file(C:\Users\Aparna\Anaconda\AprioriResults)")
for file in os.listdir(inputdir +'/AprioriOutput'):
    if file.endswith(".txt"):
        numofFiles = len(os.listdir(inputdir +'/AprioriOutput'))
        #print file.split(".")[0]
        inputFile = open(inputdir +'/AprioriOutput/'+file,'r')
        #print "inputfile is %s" % inputFile
        i=0
        output_file = open(inputdir +'/RemovedUnknown/'+file, "w")
        for line in inputFile:
            if ("Third-term-Persisted" in line or "Third-term-Not-Persisted" in line):
                i = i+1
                output_file.write(line)
        output_file.close()
        y=1
        processedfile = open(inputdir +'/RemovedUnknown/'+file, "r")
        #print "processedfile is %s" % processedfile
        itemDict = defaultdict(list)
        #tempItemDict = defaultdict(list)
        for line in processedfile:
            itemList=[]
            for x in line.split(','):
                if "(" in x:
                    itemList.extend(y.strip() for y in x.split('('))
                else:
                    itemList.append(x.strip())
                itemList[-1]=itemList[-1].replace(')','')
            itemDict[i]=itemList
            i = i-1
        minConfidence = raw_input("Please enter the value for minimum confidence")
        originalFile = open(inputdir+'/InputFiles/'+file.split(".")[0]+'.csv')#csv file
        #print "originalFile is %s" % originalFile
        csv_f = csv.reader(originalFile)
        result_file = open(inputdir+'/FinalResults/'+file, "w")#txt file
        intersection_file = open(inputdir+'/IntersectionFiles/'+file, "w")
        finalResults = defaultdict(list)
        ifinalResults = defaultdict(list)
        finalResultsdictKey = 0
        for key,value in itemDict.items():
            itemSupport = 0
            originalFile.seek(0)
            listnoSupport = itemDict[key][:-1] 
            if "Third-term-Not-Persisted" in listnoSupport:
                label = "Third-term-Not-Persisted"
                RHS_absent = "Third-term-Persisted"
                listnoSupport.remove('Third-term-Not-Persisted')
            if "Third-term-Persisted" in listnoSupport:
                label = "Third-term-Persisted"
                RHS_absent = "Third-term-Not-Persisted"
                listnoSupport.remove('Third-term-Persisted')
            count = 0
            iCount = 0#to count transactions with inverse labels
            labelOccurence = 0
            #inverselabelOccurence = 0
            totalNumberTransactions = 0
            A = 0
            cA = 0
            B = 0
            cB = 0
            C = 0
            cC = 0
            D = 0
            cD = 0
            for rows in csv_f:
                totalNumberTransactions = totalNumberTransactions + 1
                if (set(listnoSupport)<=set(rows)):
                    #print "lovely"
                    count = count+1
                if label in rows:
                    labelOccurence = labelOccurence + 1
                if label in rows and (set(listnoSupport)<=set(rows)):
                    A = A + 1
                if RHS_absent in rows and (set(listnoSupport)<=set(rows)):
                    B = B + 1
                if label in rows and not (set(listnoSupport)<=set(rows)):
                    C = C + 1
                if RHS_absent in rows and not(set(listnoSupport)<=set(rows)):
                    D = D + 1
            supportX = float(count)/totalNumberTransactions
            supportX_Y = float(itemDict[key][-1])/100
            supportY = float(labelOccurence)/totalNumberTransactions#support of Y
            chi2 = chi2Calculation.calculate(A,B,C,D) 
            xIR = (supportY - supportX)/(supportY+supportX-supportX_Y)
            IR = xIR if xIR>0 else -1*xIR
            kulc = (supportX_Y*(supportX+supportY))/(2*supportX*supportY)
            if(supportX!=0):
                if((float(supportX_Y)/supportX) > float(minConfidence)):
                    #Remove rules that have unknown
                    if not "Unknown" in str(listnoSupport):
                        finalResultsdictKey = finalResultsdictKey + 1
                        if (float(supportX_Y)/supportX > 1.0):
                            Confidence = float(1.00)
                        else:
                            Confidence = float(supportX_Y)/supportX
                        lift = float(Confidence)/supportY
                        itemList = listnoSupport[:]
                        itemList.append(label)
                        allConf = float(count)/findmax(itemList)
                        cosine = float(supportX_Y)/math.sqrt(supportX * supportY)
                        dictValue = [round(kulc,3),round(cosine,3),finalResultsdictKey,round(Confidence,3),listnoSupport,label,round(supportX_Y,3),round(lift,3),round(allConf,3),round(chi2,3),round(IR,3)]
                        finalResults[finalResultsdictKey].append(dictValue)
                        for items in listnoSupport:
                            originalFile.seek(0)
                            #contrastLists = listnoSupport[:]
                            #contrastLists.remove(items)
                            combinationValues = []
                            itemIndex = -1
                            for row in csv_f:
                                clist = list(row)
                                if items in row:
                                    itemIndex = clist.index(items)
                                else:
                                    if(itemIndex!=-1):
                                        if clist[itemIndex] not in combinationValues:
                                            combinationValues.append(clist[itemIndex])
                            originalFile.seek(0)
                            for cvalue in combinationValues:
                                contrastLists = listnoSupport[:]
                                contrastLists.remove(items)
                                contrastLists.append(cvalue)
                                originalFile.seek(0)
                                for rows in csv_f:
                                    if (set(contrastLists)<=set(rows)):
                                        iCount = iCount+1
                                    if label in rows and (set(contrastLists)<=set(rows)):
                                        cA = cA + 1
                                    if RHS_absent in rows and (set(contrastLists)<=set(rows)):
                                        cB = cB + 1
                                    if label in rows and not (set(contrastLists)<=set(rows)):
                                        cC = cC + 1
                                    if RHS_absent in rows and not(set(contrastLists)<=set(rows)):
                                        cD = cD + 1
                                isupportX_Y = float(cA)/totalNumberTransactions
                                isupportX = float(iCount)/totalNumberTransactions
                                ichi2 = chi2Calculation.calculate(cA,cB,cC,cD)
                                iIR = (supportY - isupportX)/(supportY+isupportX-isupportX_Y)
                                iIR = iIR if iIR>0 else -1*iIR
                                ikulc = (isupportX_Y*(isupportX+supportY))/(2*isupportX*supportY) if isupportX!=0 else 1
                                iConfidence = float(isupportX_Y)/isupportX if isupportX!=0 else 0
                                ilift = float(iConfidence)/supportY
                                itemList = contrastLists[:]
                                itemList.append(label)
                                iallConf = float(iCount)/findmax(itemList)
                                #iallConf = float(iCount)/labelOccurence
                                icosine = float(isupportX_Y)/math.sqrt(isupportX * supportY) if isupportX!=0 else 0
                                idictValue = [round(icosine,3),finalResultsdictKey,round(iConfidence,3),contrastLists,label,round(isupportX_Y,3),round(ilift,3),round(iallConf,3),round(ichi2,3),round(iIR,3),round(ikulc,3)]
                                ifinalResults[finalResultsdictKey].append(idictValue)
        rulesID = 0
        for key, value in finalResults.items():
            rulesID = rulesID + 1
            result_file.write("\n\n%s " % str(rulesID))#ID
            result_file.write("\t%s " % str(value[0][1]))#Cosine
            result_file.write("\t%s " % str(value[0][3]))#Confidence
            result_file.write("\t%s" % str(value[0][4]))#antecedant
            result_file.write("--->")
            result_file.write(str(value[0][5]))#consequent
            result_file.write("\t%s " % str(value[0][6]))#Support
            result_file.write("\t%s " % str(value[0][7]))#Lift
            result_file.write("\t%s " % str(value[0][8]))#All confidence
            result_file.write("\t%s " % str(value[0][9]))#Chi2
            result_file.write("\t%s " % str(value[0][10]))#IR
            result_file.write("\t%s " % str(value[0][0]))#kulc
            result_file.write("\n")
            for key1, value1 in ifinalResults.items():
                for keyItems in value1:
                    if(key==key1):
                        result_file.write("%s " % str(rulesID))#ID
                        result_file.write("\t%s " % str(keyItems[0]))#Cosine
                        result_file.write("\t%s " % str(keyItems[2]))#Confidence
                        result_file.write("\t%s" % str(keyItems[3]))#antecedant
                        result_file.write("--->")
                        result_file.write(str(keyItems[4]))#consequent
                        result_file.write("\t%s " % str(keyItems[5]))#Support
                        result_file.write("\t%s " % str(keyItems[6]))#Lift
                        result_file.write("\t%s " % str(keyItems[7]))#All confidence
                        result_file.write("\t%s " % str(keyItems[8]))#Chi2
                        result_file.write("\t%s " % str(keyItems[9]))#IR
                        result_file.write("\t%s " % str(keyItems[10]))#kulc
                        result_file.write("\n")
            intersection_file.write(str(value[0][2]))
            intersection_file.write(str(value[0][3]))
            intersection_file.write("\n")
        result_file.close()
        intersection_file.close()
rules = [set() for i in range(numofFiles)]
index = 0
'''for file in os.listdir(inputdir +'/IntersectionFiles/'):
    if file.endswith(".txt"):
        print file
        rules[index] = set(open(inputdir +'/IntersectionFiles/'+file,'r'))
        index = index + 1
intersectionRules = set.intersection(*rules)'''
'''results = open(inputdir+'/GlobalRules.txt', "w")#txt file
for item in list(intersectionRules):
    anteConse = item.split(']')
    results.write(str(anteConse[0]))
    results.write("]--->")
    results.write(str(anteConse[1]))
results.close()'''