

def get_data(square_dim, images, labels):
	images = open(images, 'r').readlines()
	labels = open(labels, 'r').readlines()
	t_images = list()
	t_labels = list()

	for i in range(len(labels)):
		temp = images[i*square_dim:i*square_dim+square_dim]
		for j in range(square_dim):
			temp[j] = list(temp[j].rstrip('\n'))
			for k in range(len(temp[j])):
				if temp[j][k] == ' ':
					temp[j][k] = 0
				else:
					temp[j][k] = 1
		t_images.append(temp)
		t_labels.append(int(labels[i]))

	return (t_images, t_labels)

if __name__ == '__main__':
	get__data(28,'../digitdata/trainingimages','../digitdata/traininglabels')
