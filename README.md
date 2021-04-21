# park-rllib
[Park](https://github.com/park-project/park) and [rllib](https://github.com/ray-project/ray/tree/master/rllib) integration
# Introduction
This is a simple integration of a reinforcement leanrning library [rllib](https://github.com/ray-project/ray/tree/master/rllib) with [Park](https://github.com/park-project/park).

# Setup the environment
## Setup the environment in your machine
1. Download source code from GitHub
   ```
    git clone https://github.com/saeid93/park-rllib
   ```
2. Download and install [miniconda](https://docs.conda.io/en/latest/miniconda.html)
3. Create [conda](https://docs.conda.io/en/latest/miniconda.html) virtual-environment
   ```
    conda create --name parkrllib python=3
   ```
4. Activate conda environment
   ```
    conda activate parkrllib
   ```
5. if you want to use GPUs make sure that you have the correct version of CUDA and cuDNN installed from [here](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html)
6. Use [PyTorch](https://pytorch.org/) or [Tensorflow](https://www.tensorflow.org/install/pip#virtual-environment-install) isntallation manual to install one of them based-on your preference

7. Install the followings
   ```
    sudo apt install cmake libz-dev
   ```
8. Install requirements
   ```
    pip install -r requirements.txt
   ```
# Project structure

* [data/](/data)
* [experiments/](/experiments)
* [park/](/park)

The code is separated into three module:

   1. [data/](/data): This is the folder containing all the configs and results of the project. Could be anywhere in the project.
   2. [/experiments](/experiments): The scripts used for using rllib.
   3. [park/](/park): The park library copied from the [park](https://github.com/park-project/park) repository.

## 1. [data/](/data)
### Structure
Link the data folder (could be placed anywhere in your harddisk) to the project. A sample of the data folder is available at [data/](./CCGrid-paper/data).


### Usage
Go to [/experiments/utils/constants.py](/experiments/utils/constants.py) and set the path to your data and project folders in the file. For example:
   ```
   DATA_PATH = "/Users/saeid/Codes/park-rllib/data"
   ```

## 2. [experiments/](experiments/)

## 3. [park/](park/)

See the [park](https://github.com/park-project/park) original repository and [paper](https://papers.nips.cc/paper/2019/hash/f69e505b08403ad2298b9f262659929a-Abstract.html).
