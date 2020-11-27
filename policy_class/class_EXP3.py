

class EXP3(object):
    def __init__(self, k):
        self.k = k
        self.gamma = 0.5
        self.epsilon = self.gamma / self.k

    def init(self):
        print('self.gamma:', self.gamma)
        print('self.epsilon:', self.epsilon)