<p float="center">
  <img src="assets/cover.png?raw=true" width="99.1%" />
</p>

# MIAS-LCEC
MIAS Group proposed a novel LiDAR-camera extrinsic calibration framework based on large vision modal and invented a cross-modal mask matching algorithm. To benifit the robotics society, we desigend MIAS-LCEC Toolbox (a versatile visual calibration toolbox) and MIAS Datasets (three real-world datasets for the evaluation of LiDAR-camera extrinsic calibration algorithms).

:pushpin: Online, Target-Free LiDAR-Camera Extrinsic Calibration via Cross-Modal Mask Matching, available at [arXiv](https://arxiv.org/abs/2404.18083).

:grapes: Toolbox versions
* **2024/07/1**: MIAS-LCEC Toolbox has been developed by Zhiwei Huang @Tongji University.

:star: **What is our contribution?** We move one step forward in the field of online, target-free LCEC by unleashing the potential of SoTA LVMs. Moreover, we invent a noval cross-modal mask matching (C3M) algorithm, enabling more robust and accurate feature corresponding for LiDAR point clouds and camera images.

:star: **What can MIAS-LCEC Toolbox do?** MIAS-LCEC Toolbox is a versatile calibration toolbox that supports **3D sensor data browsing**, **online, target-free LiDAR-camera extrinsic calibration** and **manual, offline calibration**. To start calibration, you only need to load the source file of your point cloud and image in the GUI surface and click a button. After calibration, you can view the rendered RGB point cloud using the calibrated extrinsic parameters to check the calibration result. 

<p align="center">
<img src='./assets/MIAS-LCEC-demo_3Dpointcloud.gif' width="80.0%">

</p>
*<sup> view rendered point cloud within the toolbox interface to check the visualization of calibration result</sup>*


<hr style="height:2px;border-width:0;color:gray;background-color:gray">

## 1. Publication:
This [paper (arxiv preprint)](https://arxiv.org/pdf/2005.08165.pdf) was accepted to T-IV. In this repository, we publish our toolbox software and its applicational tutorial. 

Please cite our [paper (accepted to IEEE Trans. on Intelligent Vehicles (T-IV))](https://arxiv.org/abs/2404.18083) when using our source code or datasets:
```
@article{huang2024online,
  title={Online, Target-Free LiDAR-Camera Extrinsic Calibration via Cross-Modal Mask Matching},
  author={Huang, Zhiwei and Zhang, Yikang and Chen, Qijun and Fan, Rui},
  journal={arXiv preprint arXiv:2404.18083},
  year={2024}
}
```
<hr style="height:2px;border-width:0;color:gray;background-color:gray">

## 2. Demo Video:
In this [video](https://www.youtube.com/), we demonstrated: (a) The proposed algorithm;  (b) The introduction of three real-world datasets; (c) The calibration example using our toolbox.

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
To install MIAS-LCEC Toolbox, please refer to the python package [installation introduction](./doc/installation.md).

<hr style="height:2px;border-width:0;color:gray;background-color:gray">

## 5. Getting Started
Please refer to the [user guide](./doc/program.md) for application details of this toolbox.
<hr style="height:2px;border-width:0;color:gray;background-color:gray">

## 6. Contact
Please feel free to drop me emails *zhiwei.huang@outlook.com* if you have any questions.



