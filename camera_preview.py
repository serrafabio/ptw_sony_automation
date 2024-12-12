"""

Developer: Fabio Serra Pereira (serrafabio10@outlook.com)
GOAL: aims to remote live stream the image of the camera to the computer display.

REQUIREMENT: this script require the external/crsdk folder
"""

import ctypes

path = f"C:\\Users\\serra\\OneDrive\\Documentos\\WiP\\HiWi\\Alex\\external\\crsdk\\"
file = f"monitor_protocol.dll"

my_dll = ctypes.CDLL(path+file)

my_dll.minha