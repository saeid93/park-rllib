import os
import sys
import shutil

import ray
from ray import tune
from ray.rllib.utils.framework import try_import_torch
import pprint

# get an absolute path to the directory that contains parent files
project_dir = os.path.dirname(os.path.join(os.getcwd(), __file__))
sys.path.append(os.path.normpath(os.path.join(project_dir, '..', '..')))

from experiments.utils.constants import RESULTS_PATH
from experiments.utils.callbacks import CustomCallback
from experiments.utils.params import (
    config,
    config_file_path
)
from experiments.utils.choose_cls import env_class

torch, nn = try_import_torch()


def learner():
    """
    the central learning functionalities:
        1. read the input_config
           - input_config: {"env_config_base": ...,
                            "run_or_experiment": ...,
                            "learn_config": ...,
                            "stop": ...}
        2. read all the parts of the input_config
           - env_config_base: environment configs informations
           - run_or_experiment: name of the algorithms
           - learn_config: ray learning config template
           - stop: stoping criteria of the ray
        3. make the final env_config based on the json
        4. make ray_config based-on the environment
        5. make the final ray_config
            - ray_config: {...
                            learning paramters
                           ...,
                           env: <environment class>,
                           env_config: <environment config read before>
                           }

    the results are saved into the following path:
    the path is the concatenation:
        - results path:
          data/results/
        - environment info:
          env/<env_id>/datasets/<dataset_id>/workloads/<workload_id>
          /experiments/<experiment_id>
        - rllib:
          <name_of_algorithm>/<trial>
    """
    # <----- extract differnt parts of the input_config ----->
    # metadata = input_config["metadata"]
    stop: str = config.stop
    learn_config: dict = config.learn_config
    run_or_experiment: str = config.run_or_experiment

    # <----- generate the ray_config ----->
    # make the learning config based on the type of the environment
    ray_config = {'env': env_class(config.type_env)
                  ,'env_config': {}}

    experiments_folder = os.path.join(RESULTS_PATH,
                                      "series",     str(config.series),
                                      "envs",       str(config.type_env),
                                      "experiments")

    # make the base bath if it does not exists
    if not os.path.isdir(experiments_folder):
        os.makedirs(experiments_folder)
    # generate new experiment folder
    content = os.listdir(experiments_folder)
    new_experiment = len(content)
    this_experiment_folder = os.path.join(experiments_folder,
                                          str(new_experiment))
    # make the new experiment folder
    os.mkdir(this_experiment_folder)

    # copy our input json to the path a change
    # the name to a unified name
    shutil.copy(config_file_path, this_experiment_folder)
    source_file = os.path.join(this_experiment_folder,
                               os.path.split(config_file_path)[-1])
    dest_file = os.path.join(this_experiment_folder, 'experiment_config.json')
    os.rename(source_file, dest_file)

    # update the ray_config with learn_config
    ray_config.update(learn_config)

    # if callback is specified add it here
    if config.use_callback:
        ray_config.update({'callbacks': CustomCallback})

    # run the ML after fixing the folders structres
    _ = tune.run(local_dir=this_experiment_folder,
                 run_or_experiment=run_or_experiment,
                 config=ray_config,
                 stop=stop,
                 checkpoint_freq=config.checkpoint_freq,
                 checkpoint_at_end=True)

    # delete the unnecessary big json file
    this_experiment_trials_folder = os.path.join(
        this_experiment_folder, run_or_experiment)
    this_experiment_trials_folder_contents = os.listdir(
        this_experiment_trials_folder)
    for item in this_experiment_trials_folder_contents:
        if 'json' in item:
            json_file_name = item
            break
    json_file_path = os.path.join(this_experiment_trials_folder,
                                  json_file_name)
    os.remove(json_file_path)

def main():
    """
    run it outside with
    python experiments false <-- name_of_the_config_folder -->
    e.g. for name_of_the_config_folder: PPO_1
    type_env options:
        1. load_balance
        2. abr_sim
        3. switch_scheduling
        4. simple_queue
        5. region_assignmen
    """

    pp = pprint.PrettyPrinter(indent=4)
    print('start experiments with the following config:\n')
    pp.pprint(vars(config))

    ray.init(local_mode=config.local_mode)
    learner()


if __name__ == "__main__":
    main()
