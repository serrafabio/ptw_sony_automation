"""

Developer: Fabio Serra Pereira (serrafabio10@outlook.com)
GOAL: this script connect the camera with opencv display.

REQUIREMENT: this script needs an additional software to work, available in: https://support.d-imaging.sony.co.jp/app/webcam/en/download/
NOTICE: this script only works while the camera is not connected to the RemoteCli.exe
"""
########## IMPORT PACKAGES ############
import cv2

######## CONFIGURATION ################
# select the camera image to mirror:
cam = 3

########## FUNCTIONS #################
# this function will help to identify the available camera
def list_cameras():
    index = 0
    print("Searching for available devices...")
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.isOpened():
            break
        print(f"Camera available by the index of: {index}")
        cap.release()
        index += 1

    if index == 0:
        print("None camera detected.")
# list the camera available to select the right one
list_cameras()

# connect the opencv with the following camera:
cap = cv2.VideoCapture(cam)

# if error to connect with the camera
if not cap.isOpened():
    print("Error to access the camera.")
    exit()
# check if the program is not running
# here we set a command, if the main script is running the video must be stopped
# if 0 is the value in the file, it must stop the video, otherwise it can show the video
f = open("stop_opencv.txt", 'w')
f.write("1")
value = 1
while value == 1:
    # Capture a frame
    ret, frame = cap.read()
    if ret:
        # Show the image
        cv2.imshow('Colourful image', frame)
    else:
        print("Error to get the image.")

    with open("stop_opencv.txt", 'r') as f:
        value = int(f.read())

    # verify if the key 'q' was pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        value = 0
        break

    # Verify if the windows was closed
    if cv2.getWindowProperty('Colourful image', cv2.WND_PROP_VISIBLE) < 1:
        print("Window closed by the user.")
        value = 0
        break

# Release the camera and destroy
cap.release()
cv2.destroyAllWindows()