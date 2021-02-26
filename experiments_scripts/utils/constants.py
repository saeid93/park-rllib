import os

# dfined by the user
DATA_PATH = "/home/jdoyledithencom/data-repos/park"

# generated baesd on the users' path
DATASETS_PATH = os.path.join(DATA_PATH, "datasets")
RESULTS_PATH = os.path.join(DATA_PATH, "results")
RESULTS_PATH_EXPERIMENTS = os.path.join(DATA_PATH, "results-experimental")
CONFIGS_PATH = os.path.join(DATA_PATH, "configs")
BACKUP_PATH = os.path.join(DATA_PATH, "backup")

def _create_dirs():
    """
    create directories if they don't exist
    """
    if not os.path.exists(DATASETS_PATH):
        os.makedirs(DATASETS_PATH)
    if not os.path.exists(RESULTS_PATH):
        os.makedirs(RESULTS_PATH)
    if not os.path.exists(RESULTS_PATH_EXPERIMENTS):
        os.makedirs(RESULTS_PATH_EXPERIMENTS)
    if not os.path.exists(CONFIGS_PATH):
        os.makedirs(CONFIGS_PATH)
    if not os.path.exists(BACKUP_PATH):
        os.makedirs(BACKUP_PATH)

_create_dirs()
