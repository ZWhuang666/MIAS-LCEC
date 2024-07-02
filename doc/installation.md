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
- [Pytorch]
- [MobileSAM](https://github.com/ChaoningZhang/MobileSAM)
- [timm]
- [pyautogui]
- [pygame]

## Install C++ dependencies

```bash
# Install dependencies for Iridescence
sudo apt-get install -y libglm-dev libglfw3-dev libpng-dev libjpeg-dev libeigen3-dev libboost-filesystem-dev libboost-program-options-dev

# Install Iridescence for visualization
git clone https://github.com/koide3/iridescence --recursive
mkdir iridescence/build && cd iridescence/build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
sudo make install

# in some case the LCVision can't find iridescence package, please add the /usr/local/lib into the ld.so.conf using below command
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
conda install cudatoolkit cudnn
conda install pytorch pytorch-cuda=11.8 -c pytorch -c nvidia

# install pytorch for CPU if Nvidia display card is not available
## Option 1
conda install torch
## Option 2
pip install torch
## Option 3
pip install torch-2.1.2+cpu-cp310-cp310-linux_x86_64.whl

# install MobileSam
# option1:download MobileSam and run below command
pip install -e.
# option2
pip install git+https://github.com/ChaoningZhang/MobileSAM.git

# install timm/pyautogui/pygame
pip install timm
pip install pyautogui
pip install pygame

#if the installed pytorch has a version comflication on torchvision，you need to delete your current torchvision and install again

```
## Build LCVision
Download LCVision from GitHub

```bash
cd ~/LCVision_ws/src/zvisionpython/src
gedit config.json
```

There will be the following contents in the config.json

```
...
```

Please rewrite "conda_path" and "sam_path" to your own installation location. For conda_path, e.g., you can viewe your conda environment path by

```bash
conda env list

```

For sam_path, e.g., if you download sam through GitHub at ~/MobileSAM, there should be "~/MobileSAM". 
 
