from __future__ import division
import perceptron_read as pread
import random
import operator

class Dataset:

	def __init__(self):
		self.max_epoch = 50
		self.trainimages = list()
		self.trainlabels = list()
		self.read_in()
		self.order = 'R'
		self.weights = dict()
		self.initial_weights()

	def read_in(self):
		training = pread.get_data(28,'../digitdata/trainingimages','../digitdata/traininglabels')
		testing = pread.get_data(28,'../digitdata/testimages','../digitdata/testlabels')
		self.trainimages = training[0]
		self.trainlabels = training[1]
		self.testimages = testing[0]
		self.testlabels = testing[1]

	def initial_weights(self):
		for i in range(10):
			# initialize weights as zeros
			w = [[0 for x in range(28)] for y in range(28)]
			self.weights[i] = w

	def alpha(self,epoch):
		return 1 / (1+epoch)

	def train(self):

		for epoch in range(1, self.max_epoch):
			decay_rate = self.alpha(epoch)
			correct_count = 0

			r = list(range(len(self.trainimages)))
			if self.order == 'R':
				# print 'RANDOM ORDERING'
				random.shuffle(r)
			else:
				print 'FIXED ORDERING'
			for i in r:
				cur_image = self.trainimages[i]
				cur_label = self.trainlabels[i]
				assigned_label = self.decision_rule(cur_image)
				if cur_label != assigned_label:
					for j in range(len(cur_image)):
						for k in range(len(cur_image[j])):
								self.weights[cur_label][j][k] = self.weights[cur_label][j][k] + decay_rate * cur_image[j][k]
								self.weights[assigned_label][j][k] = self.weights[assigned_label][j][k] - decay_rate * cur_image[j][k]
				else:
					correct_count+=1
			print "Epoch: ", epoch, " --> Accuracy: %g" %(correct_count / len(self.trainimages)) 
	def decision_rule(self, imagey):
		c = dict()
		for label in range(10):
			c[label] = 0
			for i in range(len(imagey)):
				for j in range(len(imagey[0])):
					xy = self.weights[label][i][j] * imagey[i][j]
					c[label] += xy
		return max(c.iteritems(), key=operator.itemgetter(1))[0]

if __name__ == '__main__':
	ds = Dataset()
	ds.train()

