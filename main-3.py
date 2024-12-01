from ptw_sony_interface import Camera, ConnectionError
import subprocess

##### CONFIGURATION #####

# path to .exe file
dir_path = r"C:\\Users\\serra\\OneDrive\\Documentos\\WiP\\HiWi\\Alex\\build\\Debug\\RemoteCli.exe"

# Set the Photo Configuration: see the documentation to find the right parameters
# set ISO
# set Shutter Speed
# set Aperture





sony_7r = Camera()
if not sony_7r.connected:
    raise ConnectionError

sony_7r.iso = 100
sony_7r.shutter_speed = 1/30


picture = sony_7r.capture