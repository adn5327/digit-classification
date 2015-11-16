import read_training as rtrain
import read_test as rtest
import plotly.plotly as py
import plotly.graph_objs as go
import math
__author__ = 'Jakub Klapacz <jklapac2@illinois.edu> and Abhishek Nigam <adnigam2@illinois.edu>'

def odds_ratio(a_class, b_class, training_data):
	atraining_matrix_obj = training_data.frequencies[a_class]
	atr_mtrx = training_data.frequencies[a_class].matrices
	acount_for_class = atraining_matrix_obj.count
	# adenominator = len(atr_mtrx) + acount_for_class * 1.0
	adenominator = acount_for_class * 1.0
	# btraining_matrix_obj = training_data.frequencies[b_class]
	# btr_mtrx = training_data.frequencies[b_class].matrices
	# bcount_for_class = btraining_matrix_obj.count
	# # bdenominator = len(btr_mtrx) + bcount_for_class * 1.0
	# bdenominator = bcount_for_class * 1.0
	frequencies = list()
	for i in range(28):
		frequencies.append(list())
		for j in range(28):
			# if tr_mtrx[1][i][j] == 0: 
				# frequencies[i].append(-10)
				# continue
			# print(atr_mtrx[1][i][j])
			# print(adenominator)
			freqa = (1 + atr_mtrx[1][i][j]) * 1.0 / adenominator
			# print(freqa)
			loga = math.log(freqa)
			# if freqa == 0: loga = -10
			# else: loga = math.log(freqa)
			# freqb = (1 + btr_mtrx[1][i][j]) * 1.0 / bdenominator
			# logb = math.log(freqb)
			# if freqb == 0: logb = -10
			# else: logb = math.log(freqb)
			# print(freqb)
			# if freqb == 0: freqb = .99999
			frequencies[i].append(loga )#/ logb)
	# print(frequencies)
	data = [
		go.Heatmap(z=frequencies)
	]
	filename = "heatmaps/digit_" + str(a_class) + ".png"
	py.image.save_as({'data': data}, filename)
	# plot_url = py.plot(data, filename=filename)

'''
	Main function
'''
def main():
	training_data = rtrain.train()
	# rtest.test(training_data)
	# odds_ratio(9, 7, training_data)
	# odds_ratio(9, 4, training_data)
	# odds_ratio(3, 5, training_data)
	# odds_ratio(3, 8, training_data)
	for i in range(10):
		odds_ratio(i, i, training_data)



if __name__ == "__main__":
	main()