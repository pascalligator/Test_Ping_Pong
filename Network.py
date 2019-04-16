from Matrix import *
from random import uniform
import Network_Vars as ntw_vars
import Sigmoid
class Network():
    def __init__(self):
        self.weights = []
        for i in range(len(ntw_vars.structure) - 1):
            self.weights.append(get_random_matrix(ntw_vars.structure[i], ntw_vars.structure[i + 1]))
        self.biases = []
        for i in range(len(ntw_vars.structure) - 1):
            self.biases.append(get_random_matrix(1, ntw_vars.structure[i + 1]))
        self.structure = ntw_vars.structure
        self.fitness = 0
    def feedforward(self, inputs):
        new_neurons = np.array([inputs])
        for i in range(len(self.structure) - 1):
            sum_without_bias = np.dot(new_neurons, self.weights[i])
            sum = np.add(sum_without_bias, self.biases[i])
            new_neurons = Sigmoid.sigmoid(sum)
        return np.ndarray.tolist(new_neurons)[0]
    def mutate(self):
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                self.weights[i][j] += uniform(-ntw_vars.mutation_size, ntw_vars.mutation_size)
        for i in range(len(self.biases)):
            self.biases[i] += uniform(-ntw_vars.mutation_size, ntw_vars.mutation_size)


