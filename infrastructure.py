import numpy as np


class hold_matrix(object):



	def increment_all(self, matrix):
		for element in matrix:
			element+=1

	def create_matrix(self):
		matrix = np.zeros((28,28), dtype=np.int)
		self.increment_all(matrix)
		return matrix

	def __init__(self):
		
		self.zero_matrix = self.create_matrix()
		self.one_matrix = self.create_matrix()
		# access elements by arr[row][column]
		# self.two_matrix = np.zeros(28,28)
	def __str__(self):
		return 'this is a hold matrix'

class digit_list(object):

	def __init__(self):

		self.frequencies = list()
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
