from gym_cloudsim.envs import (
    CloudSimV0,
    CloudSimV1,
    CloudSimV2,
    CloudSimV3,
    CloudSimV4,
    CloudSimV5,
    CloudSimV6,
)

def make_env(type_env, env_config):
    """
    make the environment object
    """
    return make_env_class(type_env)(env_config)

def make_env_class(type_env):
    """
    generate the class object
    """
    if type_env == 0:
        env = CloudSimV0
    elif type_env == 1:
        env = CloudSimV1
    elif type_env == 2:
        env = CloudSimV2
    elif type_env == 3:
        env = CloudSimV3
    elif type_env == 4:
        env = CloudSimV4
    elif type_env == 5:
        env = CloudSimV5
    elif type_env == 6:
        env = CloudSimV6
    return env

def action_pretty_print(action, env):
    if type(action) != str:
        action_formatted = action.reshape(env.num_containers,
                                          env.num_hosts)
    else:
        action_formatted = action
    return action_formatted