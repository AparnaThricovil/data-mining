from pandas import read_csv
import pandas as pd
import numpy as np
import sklearn

def findMistakes(testList,mistakeList,filename,filepath):
	#testfile=open(filepath+filename,'a')

	#write mistake in csv file
	X = pd.read_csv(filepath+filename,header=0)
	input1 = np.array(X)
	testfile = input1[testList]
	i = 0
	for item in testfile:
		item.append[mistakeList[0]]
		i = i + 1
		print item
	
	#read the closed item set processing file
	filenam = (filename).split('.')
	itemFile = open(filepath +'/apriori/FinalResults/'+filenam[0]+'.txt','r')
	result_file = open(filepath+'/'+mistake+'.txt', "w")#txt file
	#get frequent patterns
	for line in itemFile:
		itemList=[]
		check = 0
		ant = ''
		prec = ''
		for x in line.split('--->'):
			if check==1:
				prec = x
			else:
				ant = x
				check = 1
		listp = [x for x in prec.split(' ')]
		print listp[0]
		lista = [y for y in ant.split('\t')]
		print lista[-1]
		frequentItemList = lista[-1]
		frequentItemList.append[listp[0]]#antecedant and consequent
		count = 0
		mistake = 0
		#for each pattern look for the occurence in test list
		for item in testfile:
			if frequentItemList in item:
				count = count + 1
				if "Wrong" in item:
					mistake = mistake + 1
		if mistake!=0:
			probMistake = float(count)/mistake#prob of mistake = number of mistakes/number of occurence in test file
		#write result into a new file
		result_file.write(line)
		result_file.write(probMistake)
		result_file.write('\n')
	return