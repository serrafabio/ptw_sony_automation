"""

Developer: Fabio Serra Pereira (serrafabio10@outlook.com)
GOAL: here is to generate a class to control the commands of the camera

REQUIREMENT: this script only work with the RemoteCli.exe - notice to give the right path in the main function
"""
###### IMPORT PACKAGES ##########
import subprocess
import time
import threading
import queue


##### FUNCTIONS #########
# Asynchronous function foŕ the stdout
def enqueue_output(out, queue):
    for line in iter(out.readline, ''):
        queue.put(line)
    out.close()

###### CLASSES #######
class Camera():
    def __init__(self, abs_path):
        """
        Init function define parameters
        :param abs_path: dir for the RemoteCli.exe file in the build folder
        """
        # define parameters
        self.abs_path = abs_path
        self.commands = ["1\n", "1\n", "1\n", "3\n", "y\n", '0\n', '0\n', 'x\n']

    # establish connection
    def connection(self):
        """
        Establish the connection with the RemoteCli.exe software
        """
        try:
            # Initialize the subprocess
            self.process = subprocess.Popen(
                [self.abs_path],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1  # line to line
            )
        except:
            print('Failed to connect with the camera')

    def trigger_photo(self):
        # define the commands to shut a photo
        self.commands = ["1\n", "1\n", "1\n", "3\n", "y\n", '0\n', '0\n', 'x\n']
        # execute the commands
        self.execution()

    def set_ISO(self, ISO):
        # define the commands to set the ISO
        self.commands = ["1\n", "1\n", "3\n", "10\n", "y\n", f"{ISO}\n", '0\n', '0\n', 'x\n']
        # execute the commands
        self.execution()

    def set_aperture(self, aperture):
        # define the commands to set the aperture
        self.commands = ["1\n", "1\n", "3\n", "1\n", "y\n", f"{aperture}\n", '0\n', '0\n', 'x\n']
        # execute the commands
        self.execution()

    def set_shutterspeed(self, sh_speed):
        # define the commands to set the shut speed
        self.commands = ["1\n", "1\n", "3\n", "2\n", "y\n", f"{sh_speed}\n", '0\n', '0\n', 'x\n']
        # execute the commands
        self.execution()

    def execution(self):
        # start the connection
        self.connection()

        # Line to store exits
        stdout_queue = queue.Queue()
        stderr_queue = queue.Queue()

        # Threads to asynchronous reading
        stdout_thread = threading.Thread(target=enqueue_output, args=(self.process.stdout, stdout_queue))
        stderr_thread = threading.Thread(target=enqueue_output, args=(self.process.stderr, stderr_queue))
        stdout_thread.start()
        stderr_thread.start()

        try:
            for command in self.commands:
                # input the commands into the subprocess
                self.process.stdin.write(command)
                self.process.stdin.flush()

                # wait for the response of the subprocess
                time.sleep(2)

                # print the messages of the stdout
                while not stdout_queue.empty():
                    print("STDOUT:", stdout_queue.get_nowait().strip())
                while not stderr_queue.empty():
                    print("STDERR:", stderr_queue.get_nowait().strip())
        except Exception as e:
            print(f"Error to interact with the process: {e}")
        finally:
            # Close stdin and the connection
            self.process.stdin.close()
            self.process.wait()
            stdout_thread.join()
            stderr_thread.join()