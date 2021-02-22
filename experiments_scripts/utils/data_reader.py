"""
all the data reading codes in one place for
reusibility
"""
import json
import os
import pickle
import sys

# get an absolute path to the directory that contains parent files
project_dir = os.path.dirname(os.path.join(os.getcwd(), __file__))
sys.path.append(os.path.normpath(os.path.join(project_dir, '..', '..')))

from experiments_scripts.utils.constants import DATASETS_PATH


# def env_config_builder(dataset_id, workload_id):
def env_config_builder(metadata: dict, env_config_base: dict) -> dict:
    """
    read the data and workload from the disk
    and their path
    """
    # get the environment from the config file
    # env_config = config["env_config_base"]
    # metadata = config["metadata"]
    # TODO change this

    # read the necessary information from the env_config
    dataset_id = metadata["dataset_id"]
    workload_id = metadata["workload_id"]

    # dataset paths
    dataset_path = os.path.join(DATASETS_PATH, str(dataset_id))
    workload_path = os.path.join(dataset_path, "workloads", str(workload_id))

    # load dataset
    if not os.path.isdir(dataset_path):
        raise FileNotFoundError(f'dataset {dataset_id} does not exists')
    with open(os.path.join(dataset_path, 'dataset.pickle'), 'rb') as in_pickle:
        dataset = pickle.load(in_pickle)

    # load workload
    if not os.path.isdir(workload_path):
        raise FileNotFoundError((f'workload {workload_id} for dataset '
                                 f'{dataset_id} does not exists'))
    with open(os.path.join(workload_path, 'workload.pickle'),
              'rb') as in_pickle:
        workload = pickle.load(in_pickle)

    # load dataset config
    if not os.path.isdir(dataset_path):
        raise FileNotFoundError(f'dataset {dataset_id} does not exists')
    with open(os.path.join(dataset_path, 'info.json'), 'rb') as cf:
        dataset_info = json.loads(cf.read())
    hosts_cap_rng = dataset_info['hosts_cap_rng']
    containers_cap_rng = dataset_info['containers_cap_rng']

    # add additional necessary info to the config
    env_config = env_config_base
    env_config.update({'dataset': dataset,
                       'workload': workload,
                       'hosts_cap_rng': hosts_cap_rng,
                       'containers_cap_rng': containers_cap_rng})

    return env_config
