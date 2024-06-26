# Introduction
C3M is a powerful cross-modal mask matching algorithm
<p float="center">
  <img src="assets/LSCLAW.png?raw=true" width="99.1%" />
</p>

#Installation

Install pytorch (Check your cuda version and OS platform)
https://pytorch.org/get-started/locally/

Install commonly used lib:

```
pip install matplotlib opencv-python scipy timm pyautogui
```

Install commonly used lib mobileSAM for image segmentation:

```
pip install git+https://github.com/ChaoningZhang/MobileSAM.git
```

# Configuration
1. Search for ROS path:

```
python config_path.py
```

2. set config.json

```
{
    "path": {
        "ros":path of your ros python,
        "conda":path of your conda environment,
        "sam":path of SAM
    }
}
```

# Demo
Run demo script in terminal

```
python LcMatch_CApi.py
```
