'''
@author: Aparna Gopalakrishnan
Program that calls different classifiers and predicts the accuracy.
'''
from sklearn import svm
from pandas import read_csv
import pandas as pd
import numpy as np
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
import csv
import WriteResultsintoFile
import WriteMCC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn import tree
#from sklearn.calibration import CalibratedClassifierCV
from sklearn.calibration import CalibratedClassifierCV, calibration_curve
from random import randint
import MistakePatterns
import PlotROC
def callClassifiers(inputFile,truelabels,filename,outputdir):
	#,inputdir,fileExt
	print "\nInside Evaluating Classifiers with "+filename+" data set"
	outputfile=open(outputdir+'/ClassifiersResults.txt','a')
	
	X = pd.read_csv(inputFile,header=0)
	input2 = np.array(X)
	iterations = 20
	accuracySVC = 0
	accuracyKN = 0
	accuracyET = 0
	accuracyAB = 0
	accuracyNB = 0
	accuracyRF = 0
	accuracyLR = 0
	accuracyDT = 0
	while(iterations>=1):
		row_count = sum(1 for row in input2)
		trainList = []
		trainList.extend(range(0, row_count))
		testList = []
		while(len(testList)<(row_count*0.2)):
			k = randint(0,row_count-1)
			if k not in testList:
				testList.append(k)
				trainList.remove(k)
		#Splitting into Training and Test set
		input1 = input2[trainList]
		testSet = input2[testList]
		#outputfile.write('length is %f\n ' % len(input1))
		#outputfile.write('length is %f\n ' % len(testSet))
		#Splitting the labels into training and test labels
		labelFile = pd.read_csv(truelabels,header=0)
		Y = np.array(labelFile)
		train_label = Y[trainList]
		test_true_label = Y[testList]
		#outputfile.write('length is %f\n ' % len(train_label))
		#outputfile.write('length is %f\n ' % len(test_true_label))
		y = np.ravel(train_label)
		testLabel = np.ravel(test_true_label)

		
		#############################################################################

									#SVC#

		#############################################################################
		#outputfile.write('LINEAR SVC\t')
		algoName = "SVC"
		clf = svm.SVC(kernel='rbf')
		clf.fit(input1, y)
		accuracySVC = accuracySVC + clf.score(testSet, testLabel)
		#outputfile.write('Accuracy is %f\n ' % clf.score(testSet, testLabel))
		testSetPredLabel = clf.predict(testSet)
		'''mistake =[]
		for i in range(0,len(testSetPredLabel)):
			if(testSetPredLabel[i]==testLabel[i]):
				mistake.append("Right")
			else:
				mistake.append("Wrong")
		MistakePatterns.findMistakes(testList,mistake,filename+'.'+fileExt,inputdir)'''
		#if(iterations==20):
			#PlotROC.plotROCCurve(test_true_label,testSetPredLabel,outputdir+'/LearningCurve',filename)
		WriteResultsintoFile.calculatePrecisionRecallFmeasure(testLabel,testSetPredLabel,filename,outputdir,algoName)
		#WriteMCC.calculateMathewsCorrelationCoefficient(testLabel,testSetPredLabel,filename,outputdir,algoName)
		#############################################################################
									#Calibrated classiifier#

		#############################################################################
		'''outputfile.write('Calibrated classiifier\t')
		algoName = "Calibrated Classifier"
		clf = CalibratedClassifierCV(GaussianNB(),method='isotonic',cv=10)
		clf.fit(input1, y)
		outputfile.write('Accuracy is %f\n ' % clf.score(testSet, testLabel))
		#stestSetPredLabel = clf.predict(testSet)

		probability = clf.predict_proba(testSet)
		outputfile.write('Probability is')
		np.savetxt(outputfile,input1)
		for item in probability:
			outputfile.write("%f\n" % item)
		outputfile.write(np.array(probability))
		print probability
		WriteResultsintoFile.calculatePrecisionRecallFmeasure(testLabel,testSetPredLabel,filename,outputdir,algoName)
		WriteMCC.calculateMathewsCorrelationCoefficient(testLabel,testSetPredLabel,filename,outputdir,algoName)'''
		#############################################################################


								#KNeighborsClassifier#

		#############################################################################
		#outputfile.write('KNeighborsClassifier\t')
		algoName = "KNeighborsClassifier"	
		neigh = KNeighborsClassifier(n_neighbors=3)
		neigh.fit(input1, y)
		accuracyKN = accuracyKN + neigh.score(testSet, testLabel)
		#outputfile.write('Accuracy is %f\n ' % neigh.score(testSet, testLabel))	
		testSetPredLabel = neigh.predict(testSet)
		WriteResultsintoFile.calculatePrecisionRecallFmeasure(testLabel,testSetPredLabel,filename,outputdir,algoName)
		#WriteMCC.calculateMathewsCorrelationCoefficient(testLabel,testSetPredLabel,filename,outputdir,algoName)
		#############################################################################

								#ExtraTreesClassifier#

		#############################################################################
		#outputfile.write('ExtraTreesClassifier\t')
		algoName = "ExtraTreesClassifier"
		clf = ExtraTreesClassifier(n_estimators=10, max_depth=None, min_samples_split=1,
				random_state=0)
		clf.fit(input1, y)
		accuracyET = accuracyET + clf.score(testSet, testLabel)
		#outputfile.write('Accuracy is %f\n ' % clf.score(testSet, testLabel))
		testSetPredLabel = clf.predict(testSet)
		WriteResultsintoFile.calculatePrecisionRecallFmeasure(testLabel,testSetPredLabel,filename,outputdir,algoName)
		#WriteMCC.calculateMathewsCorrelationCoefficient(testLabel,testSetPredLabel,filename,outputdir,algoName)
		##############################################################################

								       #ADABOOST#

		##############################################################################
		#outputfile.write('ADABOOST\t')
		algoName = "ADABOOST"
		clf = AdaBoostClassifier(n_estimators=50)
		clf.fit(input1, y)
		accuracyAB = accuracyAB + clf.score(testSet, testLabel)
		#outputfile.write('Accuracy is %f\n ' % clf.score(testSet, testLabel))	
		testSetPredLabel = clf.predict(testSet)
		WriteResultsintoFile.calculatePrecisionRecallFmeasure(testLabel,testSetPredLabel,filename,outputdir,algoName)
		#WriteMCC.calculateMathewsCorrelationCoefficient(testLabel,testSetPredLabel,filename,outputdir,algoName)
		##############################################################################

								    #Naive Bayesian#

		##############################################################################
		#outputfile.write('Naive Bayesian\t')
		algoName = "Naive Bayesian"
		clf = GaussianNB()
		clf.fit(input1, y)
		accuracyNB = accuracyNB + clf.score(testSet, testLabel)
		#outputfile.write('Accuracy is %f\n ' % clf.score(testSet, testLabel))	
		testSetPredLabel = clf.predict(testSet)
		probPrediction = clf.predict_proba(testSet)
		#outputfile.write('Probability is')
		#np.savetxt(outputfile,input1)
		WriteResultsintoFile.calculatePrecisionRecallFmeasure(testLabel,testSetPredLabel,filename,outputdir,algoName)
		#WriteMCC.calculateMathewsCorrelationCoefficient(testLabel,testSetPredLabel,filename,outputdir,algoName)
		##############################################################################

								    #Random Forest#

		##############################################################################
		'''#outputfile.write('Random Forest\t')
		algoName = "Random Forest"
		clf = RandomForestClassifier()
		clf.fit(input1, y)
		accuracyRF = accuracyRF + clf.score(testSet, testLabel)
		#outputfile.write('Accuracy is %f\n ' % clf.score(testSet, testLabel))	
		testSetPredLabel = clf.predict(testSet)
		probPrediction = clf.predict_proba(testSet)
		#outputfile.write('Probability is')
		#np.savetxt(outputfile,input1)
		WriteResultsintoFile.calculatePrecisionRecallFmeasure(testLabel,testSetPredLabel,filename,outputdir,algoName)
		WriteMCC.calculateMathewsCorrelationCoefficient(testLabel,testSetPredLabel,filename,outputdir,algoName)'''
		##############################################################################

								    #Logistic Regression#

		##############################################################################
		'''#outputfile.write('Logistic Regression\t')
		algoName = "Logistic Regression"
		clf = LogisticRegression()
		clf.fit(input1, y)
		accuracyLR = accuracyLR + clf.score(testSet, testLabel)
		#outputfile.write('Accuracy is %f\n ' % clf.score(testSet, testLabel))	
		testSetPredLabel = clf.predict(testSet)
		probPrediction = clf.predict_proba(testSet)
		#outputfile.write('Probability is')
		#np.savetxt(outputfile,input1)
		WriteResultsintoFile.calculatePrecisionRecallFmeasure(testLabel,testSetPredLabel,filename,outputdir,algoName)
		WriteMCC.calculateMathewsCorrelationCoefficient(testLabel,testSetPredLabel,filename,outputdir,algoName)'''
		##############################################################################

								    #Decision Trees#

		##############################################################################
		'''#outputfile.write('Logistic Regression\t')
		algoName = "Decision Trees"
		clf = tree.DecisionTreeClassifier()
		clf.fit(input1, y)
		accuracyDT = accuracyDT + clf.score(testSet, testLabel)
		#outputfile.write('Accuracy is %f\n ' % clf.score(testSet, testLabel))	
		testSetPredLabel = clf.predict(testSet)
		probPrediction = clf.predict_proba(testSet)
		#outputfile.write('Probability is')
		#np.savetxt(outputfile,input1)
		WriteResultsintoFile.calculatePrecisionRecallFmeasure(testLabel,testSetPredLabel,filename,outputdir,algoName)
		WriteMCC.calculateMathewsCorrelationCoefficient(testLabel,testSetPredLabel,filename,outputdir,algoName)'''
		##############################################################################
		iterations = iterations - 1
	#outputfile.write('----------------------------\n\n')
	outputfile.write('\n'+filename+'\t')
	outputfile.write('Accuracy Linear SVC \t %f ' % (accuracySVC/20))
	outputfile.write('\n'+filename+'\t')
	outputfile.write('Accuracy K Neighbours \t %f ' % (accuracyKN/20))
	outputfile.write('\n'+filename+'\t')
	outputfile.write('Accuracy Extra Trees \t %f ' % (accuracyET/20))
	outputfile.write('\n'+filename+'\t')
	outputfile.write('Accuracy Adaboost \t %f ' % (accuracyAB/20))
	outputfile.write('\n'+filename+'\t')
	outputfile.write('Accuracy Naive Bayesian \t %f ' % (accuracyNB/20))
	#outputfile.write('\n'+filename+'\t')
	#outputfile.write('Accuracy Random Forest \t %f ' % (accuracyRF/20))
	#outputfile.write('\n'+filename+'\t')
	#outputfile.write('Accuracy Logistic Regression \t %f ' % (accuracyLR/20))
	#outputfile.write('\n'+filename+'\t')
	#outputfile.write('Accuracy Decision Trees \t %f\n ' % (accuracyDT/20))
	return input1,y