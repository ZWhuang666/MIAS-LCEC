# MIAS-LCEC
<p align="center">
  <img src="assets/cover.png?raw=true" width="95.1%" />
</p>

[MIAS Group](https://mias.group/) has developed a novel LiDAR-camera extrinsic calibration framework known as MIAS-LCEC and introduced a cross-modal mask matching (C3M) algorithm. To benefit the robotic community, we designed the MIAS-LCEC Toolbox, a versatile calibration toolbox with an interactive visualization interface, along with the MIAS-LCEC Datasets, which include three real-world datasets for evaluating LiDAR-camera extrinsic calibration algorithms.

:pushpin: *Online, Target-Free LiDAR-Camera Extrinsic Calibration via Cross-Modal Mask Matching*, available at [arXiv](https://arxiv.org/abs/2404.18083).

:grapes: Toolbox versions
* **2024/07/1**: MIAS-LCEC Toolbox has been developed by Zhiwei Huang @Tongji University.

:star: **What is our contribution?** We move one step forward in the field of online, target-free LCEC by unleashing the potential of SoTA large vision models (LVMs). Additionally, we introduce a novel cross-modal mask matching (C3M) algorithm, which enhances the robustness and accuracy of feature correspondence between LiDAR point clouds and camera images.

:star: **What can MIAS-LCEC Toolbox do?** MIAS-LCEC Toolbox is a versatile calibration toolbox that supports **3D sensor data browsing**, **online, target-free LiDAR-camera extrinsic calibration** and **manual, offline calibration**. To begin calibration, simply load your point cloud and image source files into the GUI and click a button. After calibration, you can view the rendered RGB point cloud using the calibrated extrinsic parameters to verify the results.

<p align="center">
<img src='./assets/MIAS-LCEC-demo_3Dpointcloud.gif' width="80.0%">
</p>

<center><sup> Viewing rendered point cloud within the toolbox interface to check the visualization of calibration result </sup></center>


<hr style="height:2px;border-width:0;color:gray;background-color:gray">

## 1. Publication:
This [paper](https://arxiv.org/pdf/2005.08165.pdf) was accepted to IEEE Trans. on Intelligent Vehicles (T-IV). In this repository, we publish our toolbox software and its applicational tutorial. Please cite


```
@article{huang2024online,
  title={Online, Target-Free LiDAR-Camera Extrinsic Calibration via Cross-Modal Mask Matching},
  author={Huang, Zhiwei and Zhang, Yikang and Chen, Qijun and Fan, Rui},
  journal={arXiv preprint arXiv:2404.18083},
  year={2024}
}
```

when using our toolbox or datasets.
<hr style="height:2px;border-width:0;color:gray;background-color:gray">

## 2. Demo Video:
In this video ([Bilibili Link](https://www.bilibili.com/) | [YouTube Link](https://www.youtube.com/)), we demonstrated: 
* The proposed algorithm;  
* The introduction of three real-world datasets; 
* The calibration example using MIAS-LCEC Toolbox.

<p align="center">
<img src='./assets/MIAS-LCEC-demo.gif' width="80.0%">
</p>

<hr style="height:2px;border-width:0;color:gray;background-color:gray">


## 3. Datasets
We have created the following three real-world datasets:
**MIAS-LCEC-TF70 (target-free)**, **MIAS-LCEC-CB70 (target-based)**, and **MIAS-LCEC-TF360 (target-free)**, which are now publicly available at [Google Drive](https://drive.google.com/open?id=1-9dsrJVGIpYYzdxljBMHtFychXX0BsOX&usp=drive_fs) and [BaiduDuYun](https://pan.baidu.com/s/1pYPzNmDKru4WhEcVQwgdUg?pwd=z2qg) for researchers to evaluate the performance of LCEC approaches. Two solid-state Livox LiDARs (Livox Mid-70 and Livox Mid-360) and one MindVision camera are utilized for data acquisition. Point clouds and images in the datasets are collected from a variety of indoor and outdoor environments, under various scenarios as well as different weather and illumination conditions. 

<p align="center">
<img src='./assets/dataset_demo.png' width=900px>
</p>

<!-- *<sup>...</sup>*-->

<hr style="height:2px;border-width:0;color:gray;background-color:gray">

## 4. Installation
To install MIAS-LCEC Toolbox, please refer to the [Installation Introduction](./doc/installation.md).

<hr style="height:2px;border-width:0;color:gray;background-color:gray">

## 5. Getting Started
Please refer to the [User Guide](./doc/program.md) for application details of MIAS-LCEC Toolbox.
<hr style="height:2px;border-width:0;color:gray;background-color:gray">

## 6. Contact
Please feel free to drop me emails [*zhiwei.huang@outlook.com*] if you have any questions.



