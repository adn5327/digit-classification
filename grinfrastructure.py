import numpy as np

'''
	This class is a collection of row-accessed matricies 
		of size: 28 x 28
	This matrix is initialized to all 0's
	A hold matrix has the following variables:
		matricies - a list of 28 x 28 arrays
			[0] -> zeros matrix (represents whitespace "pixel")
			[1]	-> ones matrix (represents black/gray "pixel")
		count - used with digit_list, keeps a count of how many
			times a category has been accessed
'''
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
		self.matrices.append(self.create_matrix())
		# access elements by arr[row][column]
		# self.two_matrix = np.zeros(28,28)
	def __str__(self):
		return 'this is a hold matrix'
'''
	This class creates 10 matricies - 1 for each digit category
	Variables:
				frequencies - list of hold_matricies, 1 for each 
				category 0...9
'''
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
