import numpy as np
from svm import *
import multiclass as mc
import time
import pickle 
from sys import argv

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

def main(load = 1, multiclass = 0):

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
	if multiclass == 0:
		if load:
			classifiers = pickle.load(open("perceptrons.data", "rb"))
		else:
			classifiers = list()
			for category in np.unique(y):
				start = time.clock()
				classifiers.append(SVC(category, .001))
				print classifiers[category].category_
				classifiers[category].fit(X, y)
				print "Time Elapsed:\n"
				print time.clock() - start
			pickle.dump(classifiers, open("perceptrons.data", "wb"))
			# print classifiers[category].classes_
		
		# testy, testX = process_image("../digitdata/smalltestimages", "../digitdata/smalltestlabels")
		testy, testX = process_image("../digitdata/testimages", "../digitdata/testlabels")
		# for i in range(len(testX)):
		total = 0
		correct = 0
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
			if results.index(max(results)) == testy[i]:
				correct += 1

			# print results.index(max(results))
			# print classifiers[0].predict(testX[i])
			# print classifiers[9].predict(testX[i])
		accuracy = (correct * 1.0) / (total * 1.0)
		print 'accuracy = {0:.4%}'.format(accuracy)
	else:
		if load:
			classifiers = pickle.load(open("mc.perceptrons.data", "rb"))
		else:
			classifier = mc.SVC(.001)
			classifier.fit(X, y)
			

			# for category in np.unique(y):
			# 	start = time.clock()
			# 	classifiers.append(SVC(category, .001))
			# 	print classifiers[category].category_
			# 	classifiers[category].fit(X, y)
			# 	print "Time Elapsed:\n"
			# 	print time.clock() - start
			pickle.dump(classifiers, open("mc.perceptrons.data", "wb"))
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
			results.append(classifiers[j].predict(testX[i]))
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

if __name__ == '__main__':
	start = time.clock()
	if len(argv) == 3 and argv[1] == '-r' and argv[2] == '-m':
		main(0, 1)
	elif len(argv) == 2 and argv[1] == '-r':
		main(0, 0)
	elif len(argv) == 2 and argv[1] == '-m':
		main(1, 1)
	else:
		main(1, 0)
	# main()
	print time.clock() - start