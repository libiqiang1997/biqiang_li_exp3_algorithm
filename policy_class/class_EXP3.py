import numpy as np


class EXP3(object):
    def __init__(self, name, k):
        self.name = name
        self.k = k
        self.gamma = 0.5
        self.epsilon = self.gamma / self.k

    def init(self, arms):
        # print('self.gamma:', self.gamma)
        # print('self.epsilon:', self.epsilon)
        self.weights = np.zeros(self.k)
        for i in range(len(arms)):
            self.weights[i] = arms[i].weight

    def select_arm(self):
        sum_weight_term = np.sum(self.weights)
        for i in range(len(self.weights)):
            frac_term = self.weights[i] / sum_weight_term
            first_probability_term = (1 - self.gamma) * frac_term
            second_probability_term = self.gamma / self.k
        
        # print('sum_weight_term:', sum_weight_term)
