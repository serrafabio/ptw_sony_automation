"""

Developer: Fabio Serra Pereira (serrafabio10@outlook.com)
GOAL: this is the controller script, which will start the camera controller and start and stop the opencv, if its necessary.
 The main goal is to take a photo with the camera

REQUIREMENT: this script only work with the RemoteCli.exe - notice to give the right path in the main function
"""
import time
import threading
import cv2

from ptw_sony_camera import Camera

from nanoleafapi import WHITE

from nanoleafapi import Nanoleaf, NanoleafDigitalTwin

##### CONFIGURATION #####

# path to .exe file: You need to specify the path where the build was made -  PATH OF SDK/build/Debug/RemoteCli.exe
dir_path = r"C:\\Users\\serra\\OneDrive\\Documentos\\WiP\\HiWi\\Alex\\build\\Debug\\RemoteCli.exe"

# Set the Photo Configuration: see the documentation to find the right parameters
# set the parameters configuration?
# don't forget to set the camera to the manual mode
# set ISO
ISO = "1"
# set Shutter Speed
shutter_speed= "1"
# set Aperture
aperture = "1"

# set the camera to mirror in the computer
cam = 0

# Set the IP Address of the Connection with the LEDs: API connection
IP_ADDRESS = "192.168.137.195"

'''
Set 1 for the LED to start and 0 to the LED to remain shut down
Identification of the IDs: (all considering who is observing the booth)
    1st: center in front of the observer
    2nd: first from down to up of the right side of the observer
    3rd: second from down to up of the right side of the observer
    4th: center against the side of the observer
    5th: first from down to up of the left side of the observer
    6th: second from down to up of the left side of the observer
    7th: remain 0
'''
ids = [1,1,1,1,1,1,0]

#### PARMS ####
continue_loop = True
video_active = True

def shut_photo(sony_7r):
    """
    Function to shut a picture using the camera
    :return: None
    """
    # close the opencv if it is open
    with open("stop_opencv.txt", 'w') as f:
        f.write("0")
    # wait 5 sec
    time.sleep(5)
    # shut picture
    sony_7r.trigger_photo()

def configure_specs(sony_7r):
    """
    Function to set the specifications to the camera in the MANUAL mode
    :return:None
    """
    # close the opencv if it is open
    with open("stop_opencv.txt", 'w') as f:
        f.write("0")
    # wait 5 sec
    time.sleep(5)

    # configure the parameters in the camera
    sony_7r.set_ISO(ISO)
    sony_7r.set_shutterspeed(shutter_speed)
    sony_7r.set_aperture(aperture)


def start_opencv():
    """
    Function to init the opencv package and mirror the camera display
    :return: None
    """
    # connect the opencv with the following camera:
    cap = cv2.VideoCapture(cam)

    # if error to connect with the camera
    if not cap.isOpened():
        print("Error to access the camera.")
        exit()

    # Define the resolution to the camera
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 4096)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)

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

def start_LEDs():
    """
    Function to connect with the LEDs and turn the LEDs on.
    :return: None
    """
    try:
        # Connect the Nanolead package to LEDs
        nl = Nanoleaf(IP_ADDRESS)

        # Create a digital twin to control separately each LED
        digital_twin = NanoleafDigitalTwin(nl)

        # First we start all the LEDs
        nl.power_on()  # Toggle power
        # Set all to WHITE
        nl.set_color(WHITE)  # Set colour to red
        # Set the brightness to maximum
        nl.set_brightness(100, 100)  # brightness
        # Configure the colors to each
        for i in range(len(nl.get_ids())):
            if ids[i] == 1:
                digital_twin.set_color(nl.get_ids()[i], WHITE)
            else:
                digital_twin.set_color(nl.get_ids()[i], (0, 0, 0))

        digital_twin.sync()  # Syncs with the real Nanoleaf counterpart
    except Exception as e:
        print(f"Error captured: {e}")


####### main Script #######
if __name__ == '__main__':
    print("""## Control Command  ##
        
The program can control 4 main functions: shut a photo in the camera, configure the pre-specs in the Manual mode, turn the LEDs on and mirror the camera display in 4k resolution.
        
The commands must be all given as letter to work!
        
        """)
    # start the camera
    sony_7r = Camera(dir_path)

    # start the loop
    while continue_loop:
        if video_active:
            thread_1 = threading.Thread(target=start_opencv, daemon=True)
            # display the camera image
            thread_1.start()
            time.sleep(10)

        # read the input
        inp = input("Please insert the command [s: shut picture; m: set specs in the MANUAL mode: ISO, shutter speed and aperture; l: turn the LED on; q: quit]:")

        # Conditions:
        if inp == "s":
            # shut the picture
            shut_photo(sony_7r)
            # correction to avoid to reinitialize the camera
            video_active = True
        # set the Manual SPECs in the camera
        elif inp == "m":
            # configure camera
            configure_specs(sony_7r)
            # correction to avoid to reinitialize the camera
            video_active = True
        elif inp == "l":
            # turn the LED on
            start_LEDs()
            # wait
            time.sleep(5)
            # correction to avoid to reinitialize the camera
            video_active = False
        elif inp == "q":
            # close the opencv if it is open
            with open("stop_opencv.txt", 'w') as f:
                f.write("0")
            # close program
            continue_loop = False
            # correction to avoid to reinitialize the camera
            video_active = False
        else:
            print("Command failed")
            # correction to avoid to reinitialize the camera
            video_active = False

    # close threads
    try:
        thread_1.join()
    except:
        print("Thread probably wasn't initialize")