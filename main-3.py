"""

Developer: Fabio Serra Pereira (serrafabio10@outlook.com)
GOAL: this is the controller script, which will start the camera controller and start and stop the opencv, if its necessary.
 The main goal is to take a photo with the camera

REQUIREMENT: this script only work with the RemoteCli.exe - notice to give the right path in the main function
"""
import os
import time

from ptw_sony_camera import Camera

##### CONFIGURATION #####

# path to .exe file: You need to specify the path where the build was made -  PATH OF SDK/build/Debug/RemoteCli.exe
dir_path = r"C:\\Users\\serra\\OneDrive\\Documentos\\WiP\\HiWi\\Alex\\build\\Debug\\RemoteCli.exe"

# Set the Photo Configuration: see the documentation to find the right parameters
# set the parameters configuration?
# don't forget to set the camera to the manual mode
set_parms_config = False
# set ISO
ISO = "1"
# set Shutter Speed
shutter_speed= "1"
# set Aperture
aperture = "1"

####### main Script #######
if __name__ == '__main__':
    # close the opencv if it is open
    with open("stop_opencv.txt", 'w') as f:
        f.write("0")
    # wait 5 sec
    time.sleep(5)
    # start the camera
    sony_7r = Camera(dir_path)
    # configure the parameters in the camera
    if set_parms_config:
        sony_7r.set_ISO(ISO)
        sony_7r.set_shutterspeed(shutter_speed)
        sony_7r.set_aperture(aperture)
    # shut picture
    sony_7r.trigger_photo()
    # reopen the opencv
    os.system("python .\opencv.py")