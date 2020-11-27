import numpy as np


class EXP3(object):
    def __init__(self, name, k, gamma, color):
        self.name = name
        self.k = k
        self.gamma = gamma
        self.color = color

        self.epsilon = self.gamma / self.k

    def init(self, arms):
        # print('self.gamma:', self.gamma)
        # print('self.epsilon:', self.epsilon)
        self.weights = np.zeros(self.k)
        for i in range(len(arms)):
            self.weights[i] = arms[i].weight

    def select_arm(self):
        choice = -1
        sum_weight_term = np.sum(self.weights)
        self.probabilities = np.zeros(len(self.weights))
        for i in range(len(self.weights)):
            frac_term = self.weights[i] / sum_weight_term
            first_probability_term = (1 - self.gamma) * frac_term
            second_probability_term = self.gamma / self.k
            probability = first_probability_term + second_probability_term
            self.probabilities[i] = probability
        # print('self.probabilities:', self.probabilities)
        cum_probabilities = np.cumsum(self.probabilities)
        # print('cum_probabilities:', cum_probabilities)
        prop_rand = np.random.random()
        for i in range(len(cum_probabilities)):
            if prop_rand <= cum_probabilities[i]:
                choice = i
                break
        # print('prop_rand:', prop_rand)
        # print('choice:', choice)
        return choice

    def update(self, choice, round_reward):
        modified_reward = round_reward / self.probabilities[choice]
        exponent_term = self.epsilon * modified_reward
        self.weights[choice] *= np.e ** exponent_term
        # print(self.probabilities)
