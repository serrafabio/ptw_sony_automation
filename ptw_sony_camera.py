import subprocess

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