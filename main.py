import read_training as rtrain
import read_testing as rtest

__author__ = 'Jakub Klapacz <jklapac2@illinois.edu> and Abhishek Nigam <adnigam2@illinois.edu>'


'''
	Main function
'''
def main():
	training_data = rtrain.train()
	rtest.test(training_data)

if __name__ == "__main__":
	main()