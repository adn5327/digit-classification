import numpy as np
from svm import *
import multiclass as mc
import time
import pickle 
from sys import argv
import plotly.plotly as py
# import plotly.graph_objs as go
from plotly.graph_objs import *
# Alternative classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.svm import SVC

__author__ = 'Jakub Klapacz <jklapac2@illinois.edu> and Abhishek Nigam <adnigam2@illinois.edu>'

def process_image(data_filename = "../digitdata/trainingimages", label_filename = "../digitdata/traininglabels"):
	labels = open(label_filename, "r")
	images = open(data_filename, "r")

	label_v = labels.readlines()
	y = list()
	x = list()
	for label in label_v:
		y.append(int(label))
		vectorized_image = list()
		for i in range(28):
			# line_list = list()
			cur_line = images.readline()
			# print len(cur_line)
			# print data_filename, label_filename
			for j in range(28):
				if cur_line[j] == ' ':
					vectorized_image.append(0)
				# elif cur_line[j] == '+':
					# vectorized_image.append(2)
				else:
					vectorized_image.append(1)
		x.append(vectorized_image)	
		# break

	# print y
	ret_y = np.asarray(y)
	ret_x = np.asarray(x)
	# shape = np.reshape(ret_x[1], (28, 28))
	# print shape

	# print ret_x[1]
	# print x		
	# quit()
	labels.close()
	images.close()
	return ret_y, ret_x

def main(load = 1, multiclass = 0, forest = 0):

	# Here y is a vector of labels, X is a vector of images. The same indicies of y and X correspond to one image.
	# y, X = process_image("../digitdata/smallimages", "../digitdata/smalllabels")
	y, X = process_image()
	# print np.unique(y)
	# classifier_0 = SVC(0)
	# result = classifier_0.fit(X, y)
	# testy, testX = process_image("../digitdata/smalltestimages", "../digitdata/smalltestlabels")
	
	# print result
	# for i in range(len(testX)):
	# 	print testy[i]
	# 	print 
	# 	print classifier_0.predict(testX[i])


	if forest == 1:
		for j, col in enumerate(X.T):
	    		encoder = LabelEncoder()
	    	labels = encoder.fit_transform(col)
	    	X[:, j] = labels

		X = X.astype(int)
		encoder = OneHotEncoder()
		encoded = encoder.fit_transform(X).toarray()


		# Allowing the testing set to be 0.25 of the original set
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=888)
		
		digitforest = RandomForestClassifier()
		digitforest.fit(X_train, y_train)
		digit_predictions = digitforest.predict(X_test)
		
		score = accuracy_score(y_test, digit_predictions)
		print
		print "Accuracy of Random Forest Classifier: ", score
		# print digit_predictions
		cat_sums = np.zeros(10)
		confusion_matrix = np.zeros((10,10))

		for idx in range(len(digit_predictions)):
			cat_sums[y_test[idx]] += 1
			confusion_matrix[y_test[idx]][digit_predictions[idx]] += 1
		
		for i in range(len(confusion_matrix)):
			for j in range(len(confusion_matrix[0])):
				confusion_matrix[i][j] = confusion_matrix[i][j] / cat_sums[i] * 1.0
		string = '\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9\n'
		for i in range(10):
			string += str(i) + ':\t'
			for j in range(10):
				string += '{0:.2%}\t'.format(confusion_matrix[i][j])
			string += '\n'
		
		print 
		print string	
		print 
		# matrix = confusion_matrix(y_test, digit_predictions)
		# print "Confusion matrix: \n\tE\tP\nE\t", matrix[0], "\nP\t", matrix[1]

		quit()






	if multiclass == 0:
		if load:
			classifiers = pickle.load(open("perceptrons.data", "rb"))
		else:
			classifiers = list()
			resultstats = list()
			for category in np.unique(y):
				start = time.clock()
				classifiers.append(SVC(category, .001))
			for category in np.unique(y):	
				print classifiers[category].category_
				resultstats.append(classifiers[category].fit(X, y, classifiers))
				print resultstats[category]
				print "Time Elapsed:\n"
				print time.clock() - start
			pickle.dump(classifiers, open("perceptrons.data", "wb"))
			# print classifiers[category].classes_
		
		# testy, testX = process_image("../digitdata/smalltestimages", "../digitdata/smalltestlabels")
		testy, testX = process_image("../digitdata/testimages", "../digitdata/testlabels")
		# for i in range(len(testX)):
		total = 0
		correct = 0
		confusion_matrix = np.zeros((10,10))
		category_sums = np.zeros(10)
		for i in range(len(testy)):
			# print testy[i]
			results = list()
			for j in range(len(classifiers)):
				# print j
				# print classifiers[i].bias_
				# print classifiers[i].category_
				results.append(classifiers[j].predict(testX[i]))
			# print results
			total += 1
			predicted = results.index(max(results))
			if predicted == testy[i]:
				correct += 1
			category_sums[testy[i]] += 1
			confusion_matrix[testy[i]][predicted] += 1
			# print results.index(max(results))
			# print classifiers[0].predict(testX[i])
			# print classifiers[9].predict(testX[i])
		accuracy = (correct * 1.0) / (total * 1.0)
		print 'accuracy = {0:.4%}'.format(accuracy)
		# print confusion_matrix
		for i in range(len(confusion_matrix)):
			for j in range(len(confusion_matrix[0])):
				confusion_matrix[i][j] = confusion_matrix[i][j] / category_sums[i] * 1.0
		string = '\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9\n'
		for i in range(10):
			string += str(i) + ':\t'
			for j in range(10):
				string += '{0:.2%}\t'.format(confusion_matrix[i][j])
			string += '\n'
		

		print string
		# quit()


		

	else:
		if load:
			classifiers = pickle.load(open("mc.perceptrons.data", "rb"))
		else:
			classifier = mc.SVC(.001)
			print "fitting!"
			r = classifier.fit(X, y)
			print r
			

			# for category in np.unique(y):
			# 	start = time.clock()
			# 	classifiers.append(SVC(category, .001))
			# 	print classifiers[category].category_
			# 	classifiers[category].fit(X, y)
			# 	print "Time Elapsed:\n"
			# 	print time.clock() - start
			pickle.dump(classifier, open("mc.perceptrons.data", "wb"))
			# print classifiers[category].classes_
		
		# testy, testX = process_image("../digitdata/smalltestimages", "../digitdata/smalltestlabels")
		testy, testX = process_image("../digitdata/testimages", "../digitdata/testlabels")
		# for i in range(len(testX)):
		total = 0
		correct = 0
		for i in range(len(testy)):
			# print testy[i]
			
			
				# print j
				# print classifiers[i].bias_
				# print classifiers[i].category_
			# results.append(classifier.predict(testX[i]))
			# print results
			result = classifier.predict(testX[i])
			total += 1
			if result == testy[i]:
				correct += 1

			# print results.index(max(results))
			# print classifiers[0].predict(testX[i])
			# print classifiers[9].predict(testX[i])
		accuracy = (correct * 1.0) / (total * 1.0)
		print 'accuracy = {0:.4%}'.format(accuracy)

		
	
		obj = Scatter(x = r[0][0], y = r[1][0])
			
		
			# print accuracy
			# quit()
		
			# break
		
		
		data = Data([obj])
		layout = Layout(title='Accuracy every epoch',
			xaxis = dict(
				title = "Epochs"),
			yaxis = dict(
				title = 'Accuracy'))
		fig = Figure(data=data, layout=layout)
		py.image.save_as(fig, filename='1.png')



if __name__ == '__main__':
	start = time.clock()
	
	if len(argv) == 3 and argv[1] == '-r' and argv[2] == '-m':
		main(0, 1, 0)
	elif len(argv) == 2 and argv[1] == '-r':
		main(0, 0, 0)
	elif len(argv) == 2 and argv[1] == '-m':
		main(1, 1, 0)
	elif len(argv) == 2 and argv[1] == '-f':
		main(1, 0, 1)
	else:
		main(1, 0, 0)
	# main()
	print time.clock() - start