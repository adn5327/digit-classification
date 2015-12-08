from __future__ import division
import perceptron_read as pread
import random
import math
import time
import numpy as np
from operator import itemgetter

class Dataset(object):

	def __init__(self, k_val = 5):
		self.k = k_val
		self.validation_set = 0.75
		self.read_in()
		self.predicted = list()


	def read_in(self):
		training = pread.get_data(28,'../digitdata/trainingimages','../digitdata/traininglabels')
		testing = pread.get_data(28,'../digitdata/testimages','../digitdata/testlabels')
		self.trainimages = training[0]
		self.trainlabels = training[1]
		self.testimages = testing[0]
		self.testlabels = testing[1]

	def distance(self, arr1, arr2):
		ret_val = 0
		for i in range(28):
			for j in range(28):
				ret_val += (arr1[i][j] - arr2[i][j])**2
		return math.sqrt(ret_val)

	def get_neighbors(self, point):
		distance = list()
		loop_len = int(self.validation_set * len(self.trainimages))
		for i in range(loop_len):
			idx = random.randint(0,len(self.trainimages)-1)
			train_pt = self.trainimages[idx]
			train_label = self.trainlabels[idx]
			dist = self.distance(train_pt, point)
			distance.append((train_label, dist))
		distance.sort(key=itemgetter(1))
		neighbors = list()
		for i in range(self.k):
			neighbors.append((distance[i][0], distance[i][1]))
		return neighbors

	def get_label(self, point):
		neighbor = self.get_neighbors(point)
		hits = dict()
		for i in range(len(neighbor)):
			label = neighbor[i][0]
			hits[label] = 1 + hits.get(label,0)
		sort_hit = sorted(hits.iteritems(), key=itemgetter(1), reverse=True)
		return sort_hit[0][0]
		
	def classification_rate(self):
		self.test_count = dict()
		#format will be (correct, total)
		total_correct = 0
		for label in range(10):
			self.test_count[label] = (0,0)

		for i in range(len(self.testimages)):

			cur_tuple = self.test_count[self.testlabels[i]]
			if self.predicted[i] == self.testlabels[i]:
				self.test_count[self.testlabels[i]] = (cur_tuple[0]+1, cur_tuple[1]+1)
				total_correct+=1
			else:
				self.test_count[self.testlabels[i]] = (cur_tuple[0], cur_tuple[1]+1)

		print total_correct / len(self.testlabels) 


	def confusion_matrix(self):
		matrix = np.zeros((10,10), dtype=np.double)
		for i in range(len(self.testlabels)):
			matrix[self.testlabels[i]][self.predicted[i]] += 1
		for label in range(10):
			matrix[label][:] /= self.test_count[label][1]
		np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
		print matrix
		return matrix

	def test(self):
		count = 1
		for image in self.testimages:
			# if count % 100 == 0:
			# 	print "On number %i" %(count)
			append_val = self.get_label(image)
			self.predicted.append(append_val)
			count+=1
			
		
		self.classification_rate()
		self.confusion_matrix()

def main():
	# for i in range(1,10):
	set_k = 5
	print 'k = {}'.format(set_k) 
	x=  time.clock()
	knn = Dataset(set_k)
	knn.test()
	y= time.clock()
	print y-x

if __name__ == '__main__':
	main()


