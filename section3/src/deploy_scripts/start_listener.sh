#!/bin/bash

curl -X POST http://localhost:8042/tools/execute-script --data-binary @route_dicoms.lua -v

#sudo storescp 106 -v -aet HIPPOAI -od <TODO: Put DICOM route directory here> --sort-on-study-uid st
#sudo storescp 106 -v -aet HIPPOAI -od /home/workspace/TestVolumes/Study3 --sort-on-study-uid st
storescp 106 -v -aet HIPPOAI -od /home/workspace/Study1 --sort-on-study-uid st
