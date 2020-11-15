import numpy as np
import utils as utils

class DenseLayer:
    """
    Fully connected dot products. 
    """
    def __init__(self, units=10):
        self.units = units
        self.params = {}
        self.cache = {}
        self.type = 'fc'

    def forward(self, X):
        """
        Implements forward propagation of dense layer.
        Arguments:
            X -- input data, of shape (64, 768)
        """

        # Initialize a parameter matrix if it does not exist. 
        if 'W' not in self.params:
            self.params['W'], self.params['b'] = utils.he_normal((X.shape[0], self.units))
            
        W = self.params['W']
        b = self.params['b']

        # Save the input in the cache for backpropagation.
        self.cache['A'] = X

        ### DEBUGGING
        print(f'X input shape in Dense forward prop: {X.shape}')
        print(f'W weights input shape in Dense forward prop: {W.shape}')
        print(f'b biases input shape in Dense forward prop: {b.shape}')
        
        Z = np.dot(W, X) + b

        return Z

    def backward(self, dZ, lr):
        batch_size = dZ.shape[1]
        self.cache['dW'] = np.dot(dZ, self.cache['A'].T) / batch_size
        self.cache['db'] = np.sum(dZ, axis=1, keepdims=True)
        
        # Extract the parameters.
        W = self.params['W']
        b = self.params['b']
        dW = self.cache['dW']
        db = self.cache['db']
        
        # Update parameters.
        self.params['W'] = W - lr * dW
        self.params['b'] = b - lr * db
        
        W = self.params['W']
        
        out = np.dot(W.T, dZ)
        
        ### DEBUGGING #####################################################
        print(f'dZ input shape in Dense backward: {dZ.shape}')
        print(f'out output shape in Dense backward: {out.shape}')

        return out