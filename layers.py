import numpy as np


class layer:
    def __init__(self):
        self.input = None
        self.output = None
    def forward_propagation(self,input):
        raise NotImplementedError
    def backward_propagation(self,output_error,learning_rate):
        raise NotImplementedError

class FC_layer(layer):
    #input_size = input neurons
    #output_size = output neurons
    def __init__(self, input_size, output_size):
        self.weights = np.random.rand(input_size, output_size) - 0.5
        self.bias = np.random.rand(1, output_size) - 0.5
    
