import numpy as np


class hold_matrix(object):


	def create_matrix(self):
		matrix = np.zeros((28,28), dtype=np.int)
		return matrix

	def smooth_numerators(self):
		for matrix in self.matrices:
			for element in matrix:
				element+=1


	def __init__(self):
		self.count = 0
		self.matrices = list()
		self.matrices.append(self.create_matrix())
		self.matrices.append(self.create_matrix())
		# access elements by arr[row][column]
		# self.two_matrix = np.zeros(28,28)
	def __str__(self):
		return 'this is a hold matrix'

class digit_list(object):

	def __init__(self):

		self.frequencies = list()
		self.count = 0
		for i in range(10):
			self.frequencies.append(hold_matrix())

	def __str__(self):
		strstr = ""
		for i in range(len(self.frequencies)):
			strstr += str(self.frequencies[i])
			strstr += '\n'
		return str(strstr)

def main(listy):

	print listy


if __name__ == '__main__':
	main(digit_list())
