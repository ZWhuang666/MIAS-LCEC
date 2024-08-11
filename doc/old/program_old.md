# Program details

![]()

## 1. Start the program

the program consist of two independent pacakge:
| No. | Package Name  | Function                                                             |
| :-: | :-----------: | :--------------------------------------------------------------------|
|  1  |    Zvision    | A c++ package , which is the main UI of the project                  |
|  2  | Zvisionpython | A python package, the main function is to receive command and data from Zvision package and complete the segmentation function and match function, and then send the matched points pair back to Zvision package for further PNP. |

***the Zvision package and Zvisionpython package communicate with each other through ros2 topic publishing and subscribing mechanism,there will be some problem if you run both Zvision package and Zvisionpython package in two computers in a local network since there will be two pubulishing node and subscribe node with the same name in the network. if you need to run Zvision and Zvisionpython on two or more computers at the same time, please disconnect the computers with the network***

To start the toolbox, you only need to run the shell script Zvision.sh
```bash
cd ~/Zvision
sh Zvision.sh
```

## 2. UI introduction

### 2.1 control panel

this panel includes checkboxs,inputbox and buttons for general cloud and picture control.
|    Controls                           | Function                                                          |
| :-------                              | :---------------------------------------------------------------- |
| render Mode checkboxes and inputboxes | for choose the cloud rendering mode and set the rendering params. |
| load CloudPoints Button               | load a cloud file and display. then use left/right/mid/mid press/ of the mouse to rotate and zoom the cloud |
| Rosbag2 Read Button                   | read the pcd and image in a rosbag2 file, if the checkbox Folder is selected, it can handle all the bag files in a folder, if the checkbox color is selected, all image files will be in RGB mode. |
| take picture Button                   | take a cloud picture by the cloud camera and show it in the cloud image window. |
| load image Button                     | load an image from a file and show it in the cloud image window |
| ReadJson Button                       | read a json file including pics rendering condition and intrinsic ,extrinsic, and then set the "cloud camera window" and set the intrinsic /extrinsic of the cloud camera. |
| SaveJson Button                       | save the intrinsic,extrinsic of the cloud camera, and the  pic rendering conditions to a json file. |
| Remove All Button                     | remove all loaded pictures and clouds. |

### 2.2 image matching panel

|    Controls                           | Function                                                          |
| :-------                              | :---------------------------------------------------------------- |
| load picture & render controls        | load a picture and render the picture by cloud or render the cloud by the picture |
| autocalibration controls              | automatic calibration and generate calibration report |
| manual calibration controls           | picking points from cloud and image, and then complete the manual calibration |
| checkboard calibration controls       | an offline checkboard calibration method |

### 2.3 cloud camera panel
|    Controls                           | Function                                                          |
| :-------                              | :---------------------------------------------------------------- |
| camera coordination controls          | adjust the x,y,z and rotation angles around axis for the cloud camera |
| pics rendering condition controls     | adjust the params for rendering pictures genrated by the cloud camera |
| points filter controls                | adjust the filter params for the cloud camera to filt the points      |
| speedup conditions controls           | adjust params for speedup the cloudcamera projection process          |

### 2.4 cloud camera parameters

the inputbox in the panel is to show the intrinsic,distcoeffs, extrinsic of the cloud camera

## 3. Automatic Calibration
### 3.1 Single Calibration

| step |  operation                                                                                 |
| :-:  | :-----------                                                                               |
|  1   | deselect checkbox "batch" and checkbox "jsonbatch"                                         |
|  2   | click Button "calibration"                                                                 |
|  3   | select a cloud file according to the promption                                             |
|  4   | select a image file according to the promption                                             |
|  5   | select a json file of intrinsic,config and extrinsic according to the promption            |
|  6   | the result file will be found at directory "cal" in the same directory with the cloud file |

### 3.2 Batch Calibration

when you have a group of clouds and images with same intrinsic and extrinsic, batch calibration function would be a better choice.
#### 3.2.1 File Naming Rules
to ensure the cloud and it's matching image be recognized correclty, file name shall comply with below rules:
- Cloud file and it's matching image file shall be put in the same folder.
- the essential name of the cloud and the image shall be the same.
- pcd name shall be : essential name+"_merge.pcd"
- image name shall be : essential name+"_1.png"
- example: test_merge.pcd, test_1.png, will be regarded as a pair and calibrate.

#### 3.2.2 Operation Steps
| step |  operation                                                                                         |
| :-:  | :-----------                                                                                       |
|  1   | select checkbox "batch" and deselect checkbox "jsonbatch"                                          |
|  2   | click Button "calibration"                                                                         |
|  3   | select a json file of intrinsic,config and extrinsic according to the promption                    |
|  4   | select a folder including cloud and image files                                                    |
|  6   | the result file will be found at directory "intelibatch" in the same directory with the cloud file |


### 3.3 JsonBatch Calibration
when we have a lot of clouds and images with different intrinsic and extrinsic, we can classify the files by intrinsic and extrinsic, put the files with the same intrinsic and extrinsic in one folder.
and then , we can edit a batchtesting json file, to tell the program to batch calibrate all  the files automatically.

for batchtesting json file , please read the example file "batchtestingexample.json"

#### 3.3.1 Operation Steps
| step |  operation                                                                                         |
| :-:  | :-----------                                                                                       |
|  1   | deselect checkbox "batch" and select checkbox "jsonbatch"                                          |
|  2   | click Button "calibration"                                                                         |
|  3   | select the batch testing json file according to the promption                                      |
|  4   | the result file will be found at directory you assigned in the batch testing json file             |

## 4. Manual Calibration
### 4.1 Manual Calibration
| step |  operation                                                                                         |
| :-:  | :-----------                                                                                       |
|  1   | press "load cloudPoints" button in "Control Panel" to load a cloud                                                    |
|  2   | press "Read Json" Button in"Control Panel" to load a json file including intrinsic/distcoeffs/picRenderChoice        |
|  3   | Press "load CameraSrc" Button to load a image, make sure the "undistort" checkbox is selected            |
|  4   | Press "Picking" Button, and press "set pick" button in cloud image window to set the "undistort picture" as picking image, then using right-click mouse to pick points in cloud, and using left-click 0.2S to pick points in picture. |
|  5   | Press "Manual Calibration" , then a evaluation table will appear in the cloud image window, and a testreport will be generated in the "man" folder at the same location of the cloud file |
|  6   | then you can use "render camera by cloud" and "render cloud by camera " to further observe the fusion effect |

### 4.2 Rendering Function
Rendering function is designed to observe the fusion effect of cloud and camera images.it can be used for further adjust the manual calibration results and get a better extrinsic calibration.
| step |  operation                                                                                         |
| :-:  | :-----------                                                                                       |
|  1   | press "load cloudPoints" button to load a cloud                                                    |
|  2   | press "Read Json" Button to load a json file including intrinsic/distcoeffs/picRenderChoice        |
|  3   | Press "load CameraSrc" Button to load a image, make sure the "undistort" checkbox is selected            |
|  4   | Press "Render Camera by Cloud ", a rendered picture will appeared in the cloud image window        |
|  5   | Press "Render Cloud by Camera ", the cloud will be rendered by the image                           |

## 5. Checkboard Calibration & Evaluation
### 5.1 Checkboard Calibration
Checkboard calibration function is an offline calibration method to calibrate the clouds and matching images with a checkboard.
| step |  operation                                                                                         |
| :-:  | :-----------                                                                                       |
|  1   | press "load cloudPoints" button to load a cloud                                                    |
|  2   | press "read json" button to load a json file including intrinsic/distcoeffs/picRenderChoice        |
|  3   | Press "load CameraSrc" Button to load a image, make sure the "undistort" checkbox is selected      |
|  4   | Press "CB calibration " Button                                                                     |
|  5   | select a json file of intrinsic,config and true extrinsic according to the promption               |
|  6   | the result file will be found at directory "man" in the same directory with the cloud file         |

***if the checkboard calibration results looks ugly pleasse select the "Reverse" checkbox and redo the calibration***

### 5.2 Checkboard Evaluation
CheckBoard Evaluation function can evaluate and show the project err of the checkboard corners.
| step |  operation                                                                                         |
| :-:  | :-----------                                                                                       |
|  1   | make sure the clouds/config Json and cameraSrc are loaded correctly as 5.1, or just follow the checkboard calibration |
|  2   | press "CB Evaluation" button                                                                       |
|  3   | select a calibration result json file(either CB calibration/autocalibration/manualcalibration)     |
|  4   | the "Reprojection Error Report" will display in the terminal.                                                                    |

***if the Reprojection Error value looks very big(generally greater than 50), please select the "Reverse" checkbox and redo the evaluation***

## 6. calibration config

***Calibration config is critial for geting a correct calibration result.***

### 6.1 objects in the config json file
In this program, we integrate all the configs in a json file.
- object "picRenderChoice": setting the parameters for how to take pictures of the cloud by the cloud camera
- object "cloudCamera.Intrinsic": setting the intrinsic of the cloud camera,including K matrix and DistCoeffs vector
- object "cloudCamera.Extrinsic": setting true extrinsic (R and T vec) of the real camera, the extrinsic doesn't affect the calibration result, it is only used to evalute the calibration result.
- object "cloudCamera.EulerR": it is calculated by the program throught the R and T vec.
- object "cloudCamera.WorldT": it is calculated by the program throught the R and T vec.
- object "EulerType": default value is 5, means "ZYX".

***The program will automatically calculate the EulerR and WorldT anytime we reading or write a json file, or using the json file for calibration. so the calibration will keep correct even if the EulerR and WorldT is wrong input manually.***

### 6.2 Definitions of [picRenderChoice]
the params in the picRenderChoice is to define how to take cloud pictures by the virtual camera, it's very important for calibration, please read this section carefully before starting calibration.

| No. | Params | definistion | Default Value |
| :--: | :------: | :------ | :------: |
| 1 | fourNeighbor | define if the up/down/left/right four neighbor points need to be rendered in the projected image,default is false | false |
| 2 | eightNeighbor | define if the up/down/left/right eight neighbor points need to be rendered in the projected image,default is false | true |
| 3 | baseGray | define the base gray value when calculate the gray value of the projected points | 0 |
| 4 | contrast | define the contrast of the projected points | 2 |
| 5 | lowIntensity | define the min intensity of the points to be projected | 0 |
| 6 | zMin | only the cloud points with Z value greater than zMin will be projected | -30 |
| 7 | zMax | only the cloud points with Z value less than zMax will be projected | 30 |
| 8 | xMin | only the cloud points with x value greater than xMin will be projected | -40 |
| 9 | xMax | only the cloud points with x value less than xMax will be projected | 800 |
| 10 | picWidth | the width of the virtual picture ,** it should be equal to the real camera picture width ** | 1200 |
| 11 | picHeight | the height of the virtual picture, ** it shoud be equal to the real camera picture height ** | 800 |
| 12 | samplingStep | defines the interval of sampling from the cloud points | 1 |
| 13 | dMin | only the cloud points with the Zc value greater than dMin will be projected | -10 |
| 14 | dMax | only the cloud points with the Zc value less than dMax will be projected | 800 |
| 15 | color | defines take colorfull image or gray image for the virtual camera | false |
| 16 | OMP | defines if the OMP function will be used in virtual camera | true |
| 17 | OMPthreads | defines the qty of threads used in the function | 3 |
| 18 | selfRotation | defines virtual camera rotation method | true |
| 19 | saveornot | defines if the picture will be saved or not(only effectively in manual mode) | false |

## 7. How to read the calibration report

 The calibration report is written in json format, it includes below objects:
 - trueCamera: recording the Intrinsic and Extrinsic set by the calibration config
 - calCamera: recording the calibration output Intrinsice and Extrinsic
 - Evaluation: recording all the evaluation indicators.
 - cloudCamera: recording the Intrinsic and Extrinsic of the cloud camera used to take cloud pictures in the calibration
 - matePRC: recording the setting of picRenderChoice used in the calibration, it's the same with the input config before calibration.

 main evaluation indicators
 - Er: the Errors of EulerR of the calCamera against trueCamera
 - Et: the Errors of WorldT of the calCamera against trueCamera




