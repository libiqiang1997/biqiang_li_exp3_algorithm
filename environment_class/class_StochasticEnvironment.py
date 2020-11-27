import numpy as np
from class_Arm import Arm


class StochasticEnvironment(object):
    def __init__(self, k):
        self.k = k

        self.min_unif = -1
        self.max_unif = 1

    def init(self):
        expected_rewards = np.zeros(self.k)
        self.arms = []
        for i in range(self.k):
            arm_id = i
            expected_reward = np.random.uniform(self.min_unif, self.max_unif)
            # print('expected_reward:', expected_reward)
            expected_rewards[i] = expected_reward
            arm = Arm(arm_id, expected_reward)
            self.arms.append(arm)
        # for arm in self.arms:
        #     print('id:', arm.arm_id)
        #     print('expected_reward:', arm.expected_reward)
        #     print('weight:', arm.weight)