import numpy as np


class Arm(object):
    def __init__(self, arm_id, expected_reward):
        self.arm_id = arm_id
        self.expected_reward = expected_reward

        self.weight = 1

    def pull(self, sigma_noise):
        reward = np.random.normal(self.expected_reward, sigma_noise)
        return reward