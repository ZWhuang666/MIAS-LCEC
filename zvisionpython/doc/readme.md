----ZvisionPython package的依赖安装步骤--------
因为ros2自带python环境，为了避免环境干扰，总体的方法是通过miniconda3创建一个专门用于ZvisionPython package 的环境。然后将所有依赖都装在这个环境中。最后将这个环境的路径通过envpath.py加入PYTHON路径中。

1. 安装miniconda3
   下载Miniconda3-py39_4.12.0-Linux-x86_64.sh安装包，并使用bash命令安装。
   注意：miniconda的版本低可能会导致包的编译问题。

2. 创建并激活pytorch 环境
  conda create -n pytorch_env python=3.10
  conda activate pytorch_env

**以下所有步骤都必须在pytorch_env环境下执行

3. 安装pytorch
3.1 安装CPU版 pytorch
	下载torch-2.1.2+cpu-cp310-cp310-linux_x86_64.whl，并安装
     或使用conda install torch安装


3.2 如果是双系统，有Nvidia显卡，可以安装cuda,及支持cuda的pytorch
以下均须在pytorch_env环境下执行
3.2.1. ubuntu-drivers devices 显示显卡驱动
3.2.2. sudo apt-get install XXX，根据3.2.1的推荐安装显卡驱动
3.2.3. nvidia-smi确认显卡驱动安装正确
3.2.4. conda install cudatoolkit cudnn
3.2.5. conda install pytorch pytorch-cuda=11.8 -c pytorch -c nvidia，注意cuda版本与第3.2.4条里面自动安装的cuda版本保持一致。

4. 安装MObileSAM，可以采用下述两种方法之一
4.1 下载MobileSAM_Master,进入目录，pip install -e. 安装，注意-e后面的点不能少
4.2 pip install git+https://github.com/ChaoningZhang/MobileSAM.git

5. pip install timm
6. pip install pyautogui
7. pip install pygame

如果安装的pytorch与torchvision 版本不对，需要再重新安装torchvision
For further information on the compatible versions, check https://github.com/pytorch/vision#installation for the compatibility matrix.
8. pip install torchvision==0.16

9. 关于环境的补充信息请查看envpath.py文件相关注释,

10. 速度较慢时请按照pythonupdatesource.md来替换源