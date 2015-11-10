import infrastructure as infra
import read_training as rtrain
import numpy as np
import math

def test(training_data = None):
	
	labels = open('digitdata/testlabels','r')
	representation = labels.readlines()
	images = open('digitdata/testimages', 'r')

	count = 0
	for line in representation:
		generate_probability(line, training_data, images)
		if count == 30:
			quit()
		count+=1
def get_prob(digit_class, testing_matrix , digit_matrices, smooth_factor):

	training_matrix_obj = digit_matrices.frequencies[digit_class]
	tr_mtrx = digit_matrices.frequencies[digit_class].matrices
	count_for_class = training_matrix_obj.count

	pclass = (count_for_class *1.0)/ digit_matrices.count
	denominator = (smooth_factor * len(tr_mtrx) + count_for_class) * 1.0
	cur_total = math.log(pclass)
	for i in range(28):
		for j in range(28):
			for length in range(len(tr_mtrx)):
				if testing_matrix[i][j] == length:
					idx_prob = (tr_mtrx[length][i][j] + smooth_factor)/ denominator
					stry = '' + str(math.log(idx_prob)) + ' ' + str(idx_prob)
					# print stry
					cur_total += math.log(idx_prob)
					break
	cur_total *= -1
	return cur_total




def generate_probability(line, digit_matrices, images):

	str = ''
	singular_image = list()
	for i in range(28):
		cur_line = images.readline()
		str += cur_line
		singular_image.append(list())
		for j in range(28):
			if cur_line[j] != ' ':
				singular_image[i].append(1)
			else:
				singular_image[i].append(0);

	probability_per_class = list()

	for i in range(10):
		probability_per_class.append(get_prob(i, singular_image, digit_matrices, 1))
	
	max_value = max(probability_per_class)
	max_index = probability_per_class.index(max_value) 

	print max_index



if __name__ == '__main__':
	test(rtrain.train())
