from park.envs.load_balance import LoadBalanceEnv
from park.envs.abr_sim import ABRSimEnv
from park.envs.switch_scheduling import SwitchEnv
from park.envs.simple_queue import SimpleQueueEnv
from park.envs.region_assignment import RegionAssignmentEnv
# TODO add the rest of envs here

import numpy as np
from gym import spaces
import math
from park.param import config

# TODO make a centralised funciton for all envs
# def park_to_env(cl): 
#     class _cl(cl): 
#         def __init__(self, config, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#     return _cl

class LoadBalanceEnvConv(LoadBalanceEnv):
    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def setup_space(self):
        self.obs_low = np.array([0] * (config.num_servers + 1))
        self.obs_high = np.array([config.load_balance_obs_high] * (config.num_servers + 1))
        self.observation_space = spaces.Box(
            low=self.obs_low, high=self.obs_high, dtype=np.float32)
        self.action_space = spaces.Discrete(config.num_servers)

class ABRSimEnvConv(ABRSimEnv):
    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def setup_space(self):
        self.obs_low = np.array([0] * 11)
        self.obs_high = np.array([
            10e6, 100, 100, 500, 5, 10e6, 10e6, 10e6, 10e6, 10e6, 10e6])
        self.observation_space = spaces.Box(
            low=self.obs_low, high=self.obs_high, dtype=np.float32)
        self.action_space = spaces.Discrete(6)

class SwitchEnvConv(SwitchEnv):
    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def setup_space(self):
        self.observation_space = spaces.Box(low=0, high=config.ss_state_max_queue,
            shape=(config.ss_num_ports, config.ss_num_ports))
        self.action_space = spaces.Discrete(math.factorial(config.ss_num_ports))

class SimpleQueueEnvConv(SimpleQueueEnv):
    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def setup_space(self):
        self.obs_low = np.array([0, 1])
        self.obs_high = np.array([config.sq_num_servers, 5])
        self.observation_space = spaces.Box(
            low=self.obs_low, high=self.obs_high, dtype=np.float32)
        self.action_space = spaces.Discrete(2)

class RegionAssignmentEnvConv(RegionAssignmentEnv):
    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def __setup_space(self):
        self.action_space = spaces.Discrete(8)

        witness = self.__data[0]

        # lang values represent a probability distribution over
        # the language of the account (or a mixture)
        self.__lang_space = spaces.Box(
            low=np.zeros(len(witness["language"])),
            high=np.ones(len(witness["language"])),
            dtype=np.float32,
        )

        # region created is one of the 8 regions where the account
        # was created
        self.__region_created_space = spaces.Discrete(8)

        # sites is some subset of a fixed set of 100 sites that
        # have been posted with the account creating the new page.
        self.__sites_space = spaces.PowerSet(set(range(100)))

        self.observation_space = spaces.Tuple(
            (self.__lang_space, self.__region_created_space, self.__sites_space)
        )

        # TODO this is correct, but may not be tight...
        self.reward_range = (-100, 100)

# TODO add the rest of envs here
