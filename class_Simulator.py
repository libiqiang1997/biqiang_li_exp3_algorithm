import multiprocessing as mp


class Simulator(object):
    def __init__(self, env, policies):
        self.env = env
        self.policies = policies

    def run(self, num_thread, num_mc):
        manager = mp.Manager()
        thread_regret_dict = manager.dict()
        threads = []
        thread_border = []
        thread_step = num_mc // num_thread
        for i in range(num_thread):
            thread_border.append(i * thread_step)
        thread_border.append(num_mc)
        for i in range(num_thread):
            thread_id = i
            thread_num_mc = thread_border[i+1] - thread_border[i]
            threads.append(mp.Process(target=self.run_each_thread,
                                      args=(thread_id, thread_num_mc, thread_regret_dict)))
            threads[i].start()
        for i in range(num_thread):
            threads[i].join()
        regret_dict = {}
        regret_dict = thread_regret_dict
        return regret_dict

    def run_each_thread(self, thread_id, thread_num_mc, thread_regret_dict):
        self.env.init()
        for policy in self.policies:
            policy.init()
