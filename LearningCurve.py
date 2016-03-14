'''
@author: Aparna Gopalakrishnan
Program that calls learning curve
'''
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.learning_curve import learning_curve
import os

def plotLearningCurve(X,y,fileStorePath,fileName):

	print("Inside Plot learning curve")

	#train_sizes, train_scores, test_scores =  learning_curve(ExtraTreesClassifier(n_estimators=10, 
	#	max_depth=None, min_samples_split=1,random_state=0), X, y,train_sizes = np.linspace(.001, 1.0, 5))
	train_sizes, train_scores, test_scores =  learning_curve(AdaBoostClassifier(), X, y,train_sizes = np.linspace(.001, 1.0, 5))
	
	train_scores_mean = np.mean(train_scores, axis=1)
	train_scores_std = np.std(train_scores, axis=1)
	test_scores_mean = np.mean(test_scores, axis=1)
	test_scores_std = np.std(test_scores, axis=1)

	plt.title("Learning Curve with ExtraTreesClassifier")
	plt.grid()
	plt.fill_between(train_sizes,1-(train_scores_mean - train_scores_std),1-(train_scores_mean + train_scores_std), alpha=0.1,color="r")
	plt.fill_between(train_sizes,1-(test_scores_mean - test_scores_std),1-(test_scores_mean + test_scores_std), alpha=0.1, color="g")
	plt.plot(train_sizes, 1-train_scores_mean, 'o-', color="r",label="Training set error")
	plt.plot(train_sizes, 1-test_scores_mean, 'o-', color="g",label="Cross-validation error")

	plt.legend(loc="best")
	plt.ylabel('Error')
  	plt.xlabel('Training sample size')

	if not os.path.exists(fileStorePath):
		os.makedirs(fileStorePath)

	plt.savefig(fileStorePath+'/'+fileName+'.png')
	plt.clf()#clear the figure for next loop