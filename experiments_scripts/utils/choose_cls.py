from .park_to_gym import (
    LoadBalanceEnvConv,
    ABRSimEnvConv,
    SwitchEnvConv,
    SimpleQueueEnvConv,
    RegionAssignmentEnvConv
)


def env_class(env_name):
    if env_name == 'load_balance':
        return LoadBalanceEnvConv
    if env_name == 'abr_sim':
        return ABRSimEnvConv
    if env_name == 'switch_scheduling':
        return SwitchEnvConv
    if env_name == 'simple_queue':
        return SimpleQueueEnvConv
    if env_name == 'region_assignment':
        return RegionAssignmentEnvConv
    # TODO add the rest of environments here
    else:
        raise ValueError(f"unkonwn environment name {env_name}")
