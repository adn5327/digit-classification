from __future__ import division
import numpy as np
from sklearn.utils import check_X_y, check_array
import random
import plotly.plotly as py
import plotly.graph_objs as go

__author__ = 'Jakub Klapacz <jklapac2@illinois.edu> and Abhishek Nigam <adnigam2@illinois.edu>'

class SVC(object):
    """Implements a binary classifier SVM using SGD.

    Parameters
    ----------
    reg : float
        The regularization constant

    Attributes
    ----------
    weights_ : [n_features]
        Vector representing the weights of the SVM

    bias_ : float
        Float representing the bias term of the SVM

    n_features_ : int
        The number of features in the dataset.

    n_classes_ : int
        The number of classes in the dataset.
    """

    def __init__(self, reg=1):
        self.reg = reg
        self.weights_ = list()
        self.bias_ = np.zeros((10,1))
        self.n_features_ = None
        self.classes_ = None


    def f(self, x, i):
            result = ((self.weights_[i].dot(x)) + self.bias_[i])
            # quit()
            return result

    def fit(self, X, y, validation_size=0.25, n_epochs=50, n_steps=100):
        

        """Trains the support vector machine
        """
        X, y = check_X_y(X, y)
        backup_y = y
        backup_X = X
        # Need to make sure y labels are correct
        self.classes_ = np.unique(y)
        # assert len(self.classes_) == 2

        # Converts the binary labels of y into -1 and 1.
        new_y = np.zeros((10, len(y)))
        for i in range(10):
            new_y[i][y != i] = -1
            new_y[i][y == i] = 1
        # new_y[y != self.category_] = -1
        # new_y[y == self.category_] = 1
        y = new_y

        # Shuffle the training set
        perm = np.random.permutation(len(X))
        X = X[perm]
        
        

        y = y[:, perm]

        # Create the validation set
        val_ind = len(X) * validation_size
        val_X = X[:val_ind]
        val_y = y[:][:val_ind]
        X = X[val_ind:]
        y = y[:, val_ind:]
        self.n_features_ = X.shape[1]
        # Initialize weights to between [-1, 1)
        for i in range(10):
            # self.weights_.append(np.random.random(X.shape[1]) * 2 - 1)
            self.weights_.append(np.zeros(X.shape[1]))
            # self.bias_[i] = random.random()*2-1
            self.bias_[i] = 0
        # print len(self.weights_)
        # self.bias_ = random.random()*2-1
        alpha = 1
        beta = 1

        validation_accuracy = list()
        for cur_epoch in range(n_epochs):
            step = (alpha / (cur_epoch + beta))
            for i in range(10):
                for j in range(10):
                    rand_idx = np.random.choice(np.arange(len(X)))
                    cur_X = X[rand_idx]
                    results = list()
                    for k in range(10):
                        cur_y = y[k, rand_idx]
                        # results.append(self.f(cur_X, k))
                        
                    # predicted_result = results.index(max(results))    

                        if((cur_y * self.f(cur_X, k)) >= 1):
                            grad_w = self.reg * self.weights_[k]
                            grad_b = 0
                        else:
                            grad_w = (self.reg * self.weights_[k]) - (cur_y * cur_X)
                            grad_b = -cur_y
                        self.weights_[k] = self.weights_[k] - (step * grad_w)
                        self.bias_[k] = self.bias_[k] - (step * grad_b)
            total = 0
            correct = 0
            print cur_epoch
            for val_i in range(len(backup_X)):
                total += 1
                cur_X = backup_X[val_i]
                # cur_X = val_X[val_i]
                cur_y = backup_y[val_i]
                # for j in range(10):
                    # cur_y = val_y[j, val_i]
                # print cur_X
                if (self.predict(cur_X) == cur_y):
                    correct += 1
            accuracy = (correct * 1.0) / (total * 1.0)
            validation_accuracy.append([self.reg, cur_epoch, accuracy])
        matrix = np.matrix(validation_accuracy)
        x = matrix[:, 1]
        x = x.T
        x = np.asarray(x)
        # print x[0]
        y = matrix[:, 2]
        y = y.T
        y = np.asarray(y)
        # print y[0]
        # print x.shape
        
        return (x, y)



    def predict(self, X):
        """Returns the predictions (-1 or 1) on the feature set X.
        """
        # print X
        X = np.reshape(X, (1, -1))
        # print X
        # print self.weights_
        
        X = check_array(X)
        # print X.shape[1]
        # print self.n_features_

        assert X.shape[1] == self.n_features_
        results = list()
        for i in range(10):
            results.append(self.weights_[i].dot(X.T) + self.bias_[i])
        # result = self.weights_.dot(X.T) + self.bias_
        return results.index(max(results))
        # print result
        # return result
        # assert result != 0
        # if result > 0:
            # return 1
        # else:
            # return -1