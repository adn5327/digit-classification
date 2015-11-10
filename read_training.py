import infrastructure as infra
import numpy as np
import pickle

'''
	@Param 	load 	Default = 1, determines if we should calculate
					training data or load it from disk.
	This function creates a training dataset.
'''
def train(load = 1):
	if(load):
		digit_matrices = pickle.load(open('train.data', 'rb'))
	else:
		
		
		labels = open('digitdata/traininglabels', 'r')
		representation = labels.readlines()

		images = open('digitdata/trainingimages', 'r')


		digit_matrices = infra.digit_list()
		digit_matrices.count = len(representation)

		for line in representation:
			populate_category(line, digit_matrices, images)
			
		labels.close()
		images.close()

		# x = 0
		# for each_class in digit_matrices.frequencies:
		# 	x+= each_class.count
		
		# print x	
		pickle.dump(digit_matrices, open('train.data', 'wb'))
	return digit_matrices
	
'''
	@Param	line 	line from file - this should be in integer representing
					the current image's category
			digit_matricies 	Digit-list, used to store frequency information
			imgaes 	file of "images" from which we want to generate training data
'''
def populate_category(line, digit_matrices, images):
	digit_class = int(line)
	look_at_this = digit_matrices.frequencies[digit_class].matrices
	digit_matrices.frequencies[digit_class].count+=1
	for i in range(28):
		cur_line = images.readline()
		for j in range(28):
			if cur_line[j] != ' ':
				look_at_this[1][i][j] +=1
			else:
				look_at_this[0][i][j] +=1


	


if __name__ == '__main__':
	train()