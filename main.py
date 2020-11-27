from datetime import datetime
import multiprocessing as mp
from class_Environment import StochasticEnvironment
from class_Simulator import Simulator
from policy_class.class_EXP3 import EXP3
from util import plot_regret


# model = 'debug'
# model = 'solo_parameter_mc'
model = 'tune_parameters'
if model == 'debug':
    time_horizon = 10
    num_mc = 1
    num_thread = 1
elif model == 'solo_parameter_mc':
    time_horizon = 5000
    num_mc = 100
    num_thread = 10
elif model == 'tune_parameters':
    time_horizon = 5000
    num_mc = 100
    num_thread = 5

k = 10
sigma_noise = 0.1


def run_different_parameter(thread_id, gamma):
    figure_name = ('gamma' + str(gamma)).replace('.', 'dot')
    bandit_env = StochasticEnvironment(k, sigma_noise)
    policies = [EXP3('EXP3', k, gamma, 'black')]
    simulator = Simulator(bandit_env, policies, time_horizon)
    regret_dict = simulator.run(num_thread, num_mc)
    plot_regret(figure_name, policies, regret_dict)


if __name__ == '__main__':
    start_time = datetime.now()
    print('start_time:', start_time)

    threads = []
    if model == 'debug':
        threads.append(mp.Process(target=run_different_parameter))
        threads[0].start()
        threads[0].join()
    else:
        gammas = [0.005, 0.2]
        for i in range(len(gammas)):
            thread_id = i
            threads.append(mp.Process(target=run_different_parameter,
                                      args=(thread_id, gammas[i])))
            threads[i].start()
        for thread in threads:
            thread.join()
    end_time = datetime.now()
    cost_time = end_time - start_time
    print('start_time:', start_time)
    print('end_time:', end_time)
    print('cost_time:', cost_time)