<p float="center">
  <img src="assets/cover.png?raw=true" width="99.1%" />
</p>

# LCVision (Versatile LiDAR-Camera Calibration toolbox)
Zhiwei Huang proposed a novel LiDAR-camera extrinsic calibration framework based on large vision modal and invented a cross-modal mask matching algorithm;

:pushpin: Online, Target-Free LiDAR-Camera Extrinsic Calibration via Cross-Modal Mask Matching, available at [arXiv](https://arxiv.org/abs/2404.18083).

:grapes: Toolbox versions
* **2024/07/1**: LCVision has been developed by Zhiwei Huang @Tongji University.

:star: **What can LCVision do?** LCVision is a versatile calibration toolbox, .

:star: **How to Adapt from SAM to MobileSAM?** Since MobileSAM keeps exactly the same pipeline as the original SAM, we inherit pre-processing, post-processing, and all other interfaces from the original SAM. Therefore, by assuming everything is exactly the same except for a smaller image encoder, those who use the original SAM for their projects can **adapt to MobileSAM with almost zero effort**.

<hr style="height:2px;border-width:0;color:gray;background-color:gray">

## 1. Publication:
This [paper (arxiv preprint)](https://arxiv.org/pdf/2005.08165.pdf) was accepted to RA-L and ICRA'21. In this repository, we publish our MATLAB, C++, and CUDA code. 

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
In this [video](https://www.youtube.com/), we demonstrated: (a) The proposed algorithm; (b) ; (c) The introduction of three real-world datasets; (d) The calibration example using our toolbox LCVision.

<p align="center">
<img src='./assets/MIAS-LCEC-DEMO.gif' width=500px>
</p>

<hr style="height:2px;border-width:0;color:gray;background-color:gray">


## 3. Datasets
Two solid-state Livox LiDARs (Livox Mid-70 and Livox Mid0360) and one MindVision camera are utilized for data acquisition. We have created the following three real-world datasets:
**MIAS-LCEC-TF70 (target-free)**, **MIAS-LCEC-CB70 (target-based)**, **and MIAS-LCEC-TF360 (target-free)**, which are now publicly available at [xxx](http://) for researchers to evaluate the performance of LCEC approaches.

<p align="center">
<img src='./figs/experimental_results.png' width=600px>
</p>

*<sup>(1)–(5) columns on (a), (d) and (g) rows show the 3-D mesh models, depth images, surface normal ground truth
and the experimental results obtained using FD-Mean and FD-Median SNEs (ours), respectively; (1)–(5) columns on (b), (e) and (h) rows show the angular error
maps obtained by PlaneSVD/PlanePCA, VectorSVD, AreaWeighted, AngleWeighted, and FALS SNEs, respectively; (1)–(5) columns on
(c), (f) and (i) rows show the angular error maps obtained by SRI, LINE-MOD, SNE-RoadSeg, FD-Mean and FD-Median SNEs, respectively.</sup>*

<hr style="height:2px;border-width:0;color:gray;background-color:gray">

## 4. Installation
### 4.1 LCVision GUI (C++)
For LCVision GUI, please refer to the python package [installation introduction](https://github.com/ZWhuang666/LCVision/tree/main/doc/installation.md)
### 4.2 LCVision C3M (Python)
For LCVision C3M, please refer to the python package [installation introduction](https://github.com/ZWhuang666/LCVision/tree/main/LCVisionpython)
<hr style="height:2px;border-width:0;color:gray;background-color:gray">

## 5. Getting Started
Please refer to the [user guide](https://github.com/ZWhuang666/LCVision/tree/main/doc/program.md) for application details of this toolbox.
<hr style="height:2px;border-width:0;color:gray;background-color:gray">

## 6. Contact
Please feel free to drop me emails (Zhiwei Huang, [@outlook.com](zhiwei.huang@outlook.com)) if you have any questions.



