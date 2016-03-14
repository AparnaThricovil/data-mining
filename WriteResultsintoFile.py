'''
@author: Aparna Gopalakrishnan
Program that computes precision recall and fscore and writes it into a file.
'''
from sklearn.metrics import precision_recall_fscore_support
import csv
import os.path

def calculatePrecisionRecallFmeasure(y_true,y_pred,filename,outputdir,algoName):

	#print("\nInside Calculate F-measure\n")
	
	#outputfile=open(outputdir+'/F-measure.txt','a')
	precision,recall,fmeasure,support = precision_recall_fscore_support(y_true, y_pred, average='binary')
	#outputfile.write("________________________________________")
	'''outputfile.write("\nData set : "+filename+" with "+algoName+"\n\n")
	outputfile.write("F-measure is %f\n " % fmeasure)
	outputfile.write("Precision is %f\n " % precision)
	outputfile.write("Recall is %f\n " % recall)
	outputfile.write("\n")'''
	data = []
	first = True
	if(os.path.isfile(outputdir+'/metrics.csv') == True):
		first = False
	with open(outputdir+'/metrics.csv', 'ab') as fp:
		a = csv.writer(fp, delimiter=',')
		data = [algoName,fmeasure,precision,recall,filename]
		if(first):
			a.writerow(['Algo Name','F-measure','Precision','Recall','File Name'])
		a.writerow(data)