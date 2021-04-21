import os

# dfined by the user
DATA_PATH = "/Users/saeid/Codes/park-rllib/data"

# generated baesd on the users' path
RESULTS_PATH = os.path.join(DATA_PATH, "results")
CONFIGS_PATH = os.path.join(DATA_PATH, "configs")
BACKUP_PATH = os.path.join(DATA_PATH, "backup")

def _create_dirs():
    """
    create directories if they don't exist
    """
    if not os.path.exists(RESULTS_PATH):
        os.makedirs(RESULTS_PATH)
    if not os.path.exists(CONFIGS_PATH):
        os.makedirs(CONFIGS_PATH)
    if not os.path.exists(BACKUP_PATH):
        os.makedirs(BACKUP_PATH)

_create_dirs()
