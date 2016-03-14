'''
@author: Aparna Gopalakrishnan
Program that calls ROC curve
'''
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import roc_curve, auc
import os

def plotROCCurve(y_test,y_score,fileStorePath,fileName):

	#print("Inside Plot ROC curve")
	fpr = dict()
	tpr = dict()
	roc_auc = dict()
	for i in range(1):
		fpr[i], tpr[i], _ = roc_curve(y_test[:], y_score[:])
		roc_auc[i] = auc(fpr[i], tpr[i])

	# Compute micro-average ROC curve and ROC area
	fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
	roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
	plt.figure()
	plt.plot(fpr[0], tpr[0], label='ROC curve (area = %0.2f)' % roc_auc[0])
	plt.plot([0, 1], [0, 1], 'k--')
	plt.xlim([0.0, 1.0])
	plt.ylim([0.0, 1.05])
	plt.xlabel('False Positive Rate')
	plt.ylabel('True Positive Rate')
	plt.title('Receiver operating characteristic example')
	plt.legend(loc="lower right")
	#plt.show()
	if not os.path.exists(fileStorePath):
		os.makedirs(fileStorePath)
	plt.savefig(fileStorePath+'/'+'ROC'+fileName+'.png')
	plt.clf()#clear the figure for next loop

	