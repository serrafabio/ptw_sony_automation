from ptw_sony_interface import Camera, ConnectionError
import subprocess

# path to .exe file
dir_path = r"C:\\Users\\serra\\OneDrive\\Documentos\\WiP\\HiWi\\Alex\\build\\Debug\\RemoteCli.exe"


class Camera():
    def __init__(self, abs_path):
        self.abs_path = abs_path
        x = self.connection()
        if x == 0:
            self.start_menu()
        else:
            return 1

    # establish connection
    def connection(self):
        try:
            # Inicia o subprocesso
            self.process = subprocess.Popen(
                [self.abs_path],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1  # Linha a linha
            )
            return 0
        except:
            print('Failed to connect with the camera')
            return 1

    def start_menu(self):
        pass


sony_7r = Camera()
if not sony_7r.connected:
    raise ConnectionError

sony_7r.iso = 100
sony_7r.shutter_speed = 1/30


picture = sony_7r.capture