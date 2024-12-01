"""

Developer: Fabio Serra Pereira (serrafabio10@outlook.com)
GOAL: this script control via API the Nanoleaf LEDs. The goal is to control separately each LED.

"""
########## IMPORT PACKAGES ############

from nanoleafapi import discovery
from nanoleafapi import Nanoleaf

from nanoleafapi import RED, ORANGE, YELLOW, GREEN, LIGHT_BLUE, BLUE, PINK, PURPLE, WHITE

from nanoleafapi import Nanoleaf, NanoleafDigitalTwin

############# CONFIGURATION ##############

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

############## AUTOMATION ##############

# Connect the Nanolead package to LEDs
nl = Nanoleaf(IP_ADDRESS)

# Create a digital twin to control separately each LED
digital_twin = NanoleafDigitalTwin(nl)

# First we start all the LEDs
nl.power_on()             # Toggle power
# Set all to WHITE
nl.set_color(WHITE)     # Set colour to red
# Set the brightness to maximum
nl.set_brightness(100, 100) # brightness
# Configure the colors to each
for i in range(len(nl.get_ids())):
    if ids[i] == 1:
        digital_twin.set_color(nl.get_ids()[i], WHITE)
    else:
        digital_twin.set_color(nl.get_ids()[i], (0,0,0))

digital_twin.sync()    # Syncs with the real Nanoleaf counterpart

