# Installation

This project consists of two different codes package, C++and Python, and requires the installation of dependencies for both C++ and Python
## Suggestion Operation System
- ubuntu 22.04
- Ros2 humble

## C++ Dependencies

- [ROS2](https://www.ros.org/)
- [PCL](https://pointclouds.org/)
- [OpenCV](https://opencv.org/)

- [Iridescence](https://github.com/koide3/iridescence)
- [GLFW](https://www.glfw.org/) ([zlib/libpng license](https://www.glfw.org/license.html))
- [gl3w](https://github.com/skaslev/gl3w) ([Public domain](https://github.com/skaslev/gl3w/blob/master/UNLICENSE))
- [Dear ImGui](https://github.com/ocornut/imgui) ([MIT license](https://github.com/ocornut/imgui/blob/master/LICENSE.txt))
- [ImGuizmo](https://github.com/CedricGuillemet/ImGuizmo) ([MIT license](https://github.com/CedricGuillemet/ImGuizmo/blob/master/LICENSE))
- [implot](https://github.com/epezent/implot) ([MIT license](https://github.com/epezent/implot/blob/master/LICENSE))
- [Eigen](https://eigen.tuxfamily.org/index.php) ([MPL2 license](https://www.mozilla.org/en-US/MPL/2.0/))
- [portable-file-dialogs](https://github.com/samhocevar/portable-file-dialogs) ([WTFPL license](https://github.com/samhocevar/portable-file-dialogs/blob/main/COPYING))
## Python Dependencies
- [Pytorch](https://pytorch.org/get-started/locally/)
- [MobileSAM](https://github.com/ChaoningZhang/MobileSAM)
- timm

## Install C++ dependencies

```bash
# Install dependencies for Iridescence
sudo apt-get install -y libglm-dev libglfw3-dev libpng-dev libjpeg-dev libeigen3-dev libboost-filesystem-dev libboost-program-options-dev

# Install Iridescence for visualization
##Option1,copy the iridescence attched with this software to your computer
mkdir iridescence/build && cd iridescence/build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
sudo make install
##option2, download iridescence.this method might have some problem if iridescence updated.
git clone https://github.com/koide3/iridescence --recursive
mkdir iridescence/build && cd iridescence/build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
sudo make install

# in some case the zvision can't find iridescence package, please add the /usr/local/lib into the ld.so.conf using below command
sudo vim /etc/ld.so.conf

# make the config into effective
sudo /sbin/ldconfig -v
```
## Install Python Environments

***A new environment must be created and all the dependencies shall be installed under this environment, this document use pytorch_env as the environment name , users can change this environment name***

```bash
# Install miniconda3
# download Miniconda3-py39_4.12.0-Linux-x86_64.sh from website
bash Miniconda3-py39_4.12.0-Linux-x86_64.sh

# create and activate pytorch environment
# make sure the python version consistent with the python version of ROS2
conda create -n pytorch_env python=3.10
conda activate pytorch_env

# install pytorch and cuda in the pytorch environment
# make sure the cuda version keep consistent in below two commands
# make sure the Nvida driver is installed correctly
nvidia-smi
conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=11.8 -c pytorch -c nvidia

# install pytorch for CPU if Nvidia display card is not available
## Option 1
conda install torch
## Option 2
pip install torch
## Option 3
pip install torch-2.1.2+cpu-cp310-cp310-linux_x86_64.whl

# install MobileSam
# option1:download MobileSam and run below command
cd ~/MIAS-LCEC/bin/MobileSAM
pip install -e.
# option2
pip install git+https://github.com/ChaoningZhang/MobileSAM.git

# install timm/pyautogui/pygame
pip install timm
```

## Build MIAS-LCEC
Download MIAS-LCEC from GitHub

```bash
# clone git source
cd ~
git clone https://github.com/ZWhuang666/MIAS-LCEC.git
cd ~/MIAS-LCEC/

# activate your conda environment and make the configurtaion
conda activate pytorch_env
python config.py
```

The above process will download MIAS-LCEC and config the environment path of the program. If correctly operated, the file ***"~/MIAS-LCEC/bin/python/config.json"*** will be like:
```json
{
    "path": {
        "ros": "/bin/python",
        "conda": "your path to conda/envs/pytorch_env/lib/python3.10/site-packages",
        "sam": "~/MIAS-LCEC/bin/MobileSAM",
    },
    "Debug": {}
}
```

Please make sure to do ***conda activate [your conda path]*** before tapping ***python config.py***. If the program failed to run python code, please check your conda environment path using:

```bash
conda env list
```

and write the correct path to ***"~/MIAS-LCEC/bin/python/config.json"*** manually.