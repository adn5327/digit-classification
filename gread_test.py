import grinfrastructure as infra
import gread_training as rtrain
import numpy as np
import math
import time
correct_count = 0
correct_per_class = list()
num_per_class = list()
confusion_matrix = np.zeros((10,10))

'''
	@Param	training_data	Digit-list object that holds frequencies
							for categories we are training our data on
	This function categorizes 'images' based on training information 
		provided
'''
def test(training_data = None):

	for i in range(10):
		correct_per_class.append(0)
		num_per_class.append(0)	

	# labels = open('digitdata/traininglabels','r')
	labels = open('digitdata/testlabels','r')
	representation = labels.readlines()
	# images = open('digitdata/trainingimages', 'r')
	images = open('digitdata/testimages', 'r')
	count = 0
	
	
	for line in representation:
		generate_probability(line, training_data, images)
		count+=1
		# if count == 10:
		# 	break

	print (1.0 * correct_count) / count
	for i in range(len(num_per_class)):
		if(num_per_class[i] == 0):
			print(i, 0.0)
		else:
			print (i, (1.0 * correct_per_class[i]) / (num_per_class[i]) , correct_per_class[i], num_per_class[i])
	for i in range(len(confusion_matrix)):
		cat_sum = 0
		for j in range(len(confusion_matrix[0])):
			cat_sum += confusion_matrix[i][j]
		for j in range(len(confusion_matrix[0])):
			confusion_matrix[i][j] = confusion_matrix[i][j] / cat_sum * 1.0
	string = '\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9\n'
	for i in range(10):
		string += str(i) + ':\t'
		for j in range(10):
			string += '{0:.2%}\t'.format(confusion_matrix[i][j])
		string += '\n'
	print string
'''
	@Param	digit_class 	integer index of the category we want
			testing_matrix	28x28 matrix representation of an image
							we want to categorize
			digit_matricies	Digit-list object storing training data
			smooth_factor	integer representing how much smoothing to include
	@Return	cur_total 		Returns the probability testing_matrix is in digit_class

	This function computes the probability a given image (in the form 
		of a 28x28 test matrix) is in a certain category
'''
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
	# cur_total *= -1
	return cur_total

'''
	@Param 	line 			string, this should correspond to a line in testlabels
			digit_matricies	Digit-list storing training data
			images 			file to read "images" from
	This function reads in an image from the images file and computes probabilities
		for all possible categories.	
'''
def generate_probability(line, digit_matrices, images):

	str = ''
	singular_image = list()
	for i in range(28):
		cur_line = images.readline()
		str += cur_line
		singular_image.append(list())
		for j in range(28):
			if cur_line[j] == ' ':
				singular_image[i].append(0)
			elif cur_line[j] == '#':
				singular_image[i].append(1)
			else:
				singular_image[i].append(2)
	probability_per_class = list()

	for i in range(10):
		probability_per_class.append(get_prob(i, singular_image, digit_matrices, 1))
	
	max_value = max(probability_per_class)
	max_index = probability_per_class.index(max_value) 

	digit_class = int(line)
	global num_per_class
	global correct_count
	global correct_per_class
	global confusion_matrix
	num_per_class[digit_class] +=1
	confusion_matrix[digit_class][max_index] += 1
	if max_index == digit_class:
		correct_count+=1
		correct_per_class[max_index]+=1
	# print (max_index, digit_class)



if __name__ == '__main__':
	start = time.clock()
	test(rtrain.train())
	print time.clock() - start
