import face_infrastructure as infra
import face_train as rtrain
import numpy as np
import math

correct_count = 0
correct_per_class = list()
num_per_class = list()
confusion_matrix = np.zeros((2,2))

def test(training_data = None):

	for i in range(2):
		correct_per_class.append(0)
		num_per_class.append(0)	

	labels = open('facedata/facedatatestlabels','r')
	representation = labels.readlines()
	images = open('facedata/facedatatest', 'r')

	count = 0
	
	
	for line in representation:
		generate_probability(line, training_data, images)
		count+=1

	print (1.0 * correct_count) / count
	for i in range(len(num_per_class)):
		print (i, (1.0 * correct_per_class[i]) / (num_per_class[i]) , correct_per_class[i], num_per_class[i])
	for i in range(len(confusion_matrix)):
		cat_sum = 0
		for j in range(len(confusion_matrix[0])):
			cat_sum += confusion_matrix[i][j]
		for j in range(len(confusion_matrix[0])):
			confusion_matrix[i][j] = confusion_matrix[i][j] / cat_sum * 1.0
	string = '\t0\t1\n'
	for i in range(2):
		string += str(i) + ':\t'
		for j in range(10):
			string += '{0:.2%}\t'.format(confusion_matrix[i][j])
		string += '\n'
	print string

def get_prob(digit_class, testing_matrix , digit_matrices, smooth_factor):

	training_matrix_obj = digit_matrices.frequencies[digit_class]
	tr_mtrx = digit_matrices.frequencies[digit_class].matrices
	count_for_class = training_matrix_obj.count

	pclass = (count_for_class *1.0)/ digit_matrices.count
	denominator = (smooth_factor * len(tr_mtrx) + count_for_class) * 1.0
	cur_total = math.log(pclass)
	for i in range(70):
		for j in range(60):
			for length in range(len(tr_mtrx)):
				if testing_matrix[i][j] == length:
					idx_prob = (tr_mtrx[length][i][j] + smooth_factor)/ denominator
					stry = '' + str(math.log(idx_prob)) + ' ' + str(idx_prob)
					# print stry
					cur_total += math.log(idx_prob)
					break
	# cur_total *= -1
	return cur_total




def generate_probability(line, digit_matrices, images):

	str = ''
	singular_image = list()
	for i in range(70):
		cur_line = images.readline()
		str += cur_line
		singular_image.append(list())
		for j in range(60):
			if cur_line[j] != ' ':
				singular_image[i].append(1)
			else:
				singular_image[i].append(0);
	probability_per_class = list()

	for i in range(2):
		probability_per_class.append(get_prob(i, singular_image, digit_matrices, 1))
	
	max_value = max(probability_per_class)
	max_index = probability_per_class.index(max_value) 

	digit_class = int(line)
	global num_per_class
	global correct_count
	global correct_per_class
	num_per_class[digit_class] +=1
	if max_index == digit_class:
		correct_count+=1
		correct_per_class[max_index]+=1
	# print (max_index, digit_class)



if __name__ == '__main__':
	test(rtrain.train())
