from datetime import datetime
import multiprocessing as mp
from environment_class.class_StochasticEnvironment import StochasticEnvironment
from class_Simulator import Simulator
from policy_class.class_EXP3 import EXP3
from util import plot_regret


debug = True
# debug = False
if debug:
    time_horizon = 10
    num_mc = 1
    num_thread = 1
    # time_horizon = 10
    # num_mc = 10
    # num_thread = 3
else:
    time_horizon = 10
    num_mc = 10
    num_thread = 3

k = 2


def run_different_parameter():
    figure_name = ('exp3_algorithm')
    bandit_env = StochasticEnvironment(k)
    policies = [EXP3('EXP3', k)]
    simulator = Simulator(bandit_env, policies, time_horizon)
    regret_dict = simulator.run(num_thread, num_mc)
    plot_regret(figure_name)


if __name__ == '__main__':
    start_time = datetime.now()
    print('start_time:', start_time)

    threads = []
    if debug:
        threads.append(mp.Process(target=run_different_parameter))
        threads[0].start()
        threads[0].join()

    end_time = datetime.now()
    cost_time = end_time - start_time
    print('start_time:', start_time)
    print('end_time:', end_time)
    print('cost_time:', cost_time)