import argparse
import json
import os
import sys
from park.param import parser

# get an absolute path to the directory that contains parent files
project_dir = os.path.dirname(os.path.join(os.getcwd(), __file__))
sys.path.append(os.path.normpath(os.path.join(project_dir, '..', '..')))

from experiments_scripts.utils.constants import CONFIGS_PATH


# -- Basic --
parser.add_argument('--mode', type=str, default='experimental',
                    help='mode of the experiments')
parser.add_argument('--local_mode', type=bool, default=True,
                    help='whether activate the local mode of rllib or not')
parser.add_argument('--config_folder', type=str, default='',
                    help='the folder of the experiment config')
parser.add_argument('--series', type=int, default=1,
                    help='series of the experiments')
parser.add_argument('--type_env', type=str, default='load_balance',
                    help='type of the park environment')
parser.add_argument('--use_callback', type=bool, default=False,
                    help='using the callbacks or not')
parser.add_argument('--checkpoint_freq', type=int, default=100,
                    help='how often (per what number of iteration) checkpoint the results')


config, _ = parser.parse_known_args()

# read the config file
config_file_path = os.path.join(CONFIGS_PATH, config.mode,
                                config.config_folder,
                                "config_run.json")
with open(config_file_path) as cf:
    learn_config_file = json.loads(cf.read())

config_dict = vars(config)
config_dict.update(learn_config_file)
