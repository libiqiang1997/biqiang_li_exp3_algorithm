import numpy as np
from class_Arm import Arm


class StochasticEnvironment(object):
    def __init__(self, k, sigma_noise):
        self.k = k
        self.sigma_noise = sigma_noise

        self.min_unif = -1
        self.max_unif = 1

    def init(self):
        self.expected_rewards = np.zeros(self.k)
        self.arms = []
        for i in range(self.k):
            arm_id = i
            expected_reward = np.random.uniform(self.min_unif, self.max_unif)
            # print('expected_reward:', expected_reward)
            self.expected_rewards[i] = expected_reward
            arm = Arm(arm_id, expected_reward)
            self.arms.append(arm)
        # print('self.expected_rewards:', self.expected_rewards)
        # for arm in self.arms:
        #     print('id:', arm.arm_id)
        #     print('expected_reward:', arm.expected_reward)
        #     print('weight:', arm.weight)

    def get_optimal_expected_reward(self):
        optimal_expected_reward = np.max(self.expected_rewards)
        return optimal_expected_reward

    def get_selected_expected_reward(self, choice):
        selected_expected_reward = self.expected_rewards[choice]
        return selected_expected_reward

    def play(self, choice):
        round_reward = self.arms[choice].pull(self.sigma_noise)
        return round_reward