#!/bin/bash
# Run script for Zvision LiDAR-camera calibration toolbox
# obtain the script path
SCRIPT_PATH=$(realpath "$0")

# obatin the absolute path of this script
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")

/bin/python3 $SCRIPT_DIR/bin/python/lcvisionpython.py & $SCRIPT_DIR/bin/C/iviewer
