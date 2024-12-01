# This is a sample Python script.
import os
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import subprocess
import time


def photo_subprocess(process):
    # Shut photo
    process.stdin.write("3\n")
    process.stdin.flush()
    # photo
    process.stdin.write("y\n")
    process.stdin.flush()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # executable file
    dir_path = r"C:\\Users\\serra\\OneDrive\\Documentos\\WiP\\HiWi\\Alex\\"
    abs_path = dir_path + r"build\\Debug\\RemoteCli.exe"
    number_of_photos = 24
    take_one_photo = True
    # Connect with input command line
    process = subprocess.Popen([abs_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        # Enviar o comando "1" e pressionar ENTER
        process.stdin.write("1\n")
        process.stdin.flush()
        time.sleep(4)
        # Connect Remote control mode
        process.stdin.write("1\n")
        process.stdin.flush()
        time.sleep(4)
        # shutter release
        process.stdin.write("1\n")
        process.stdin.flush()
        time.sleep(4)
        # Shut photo
        process.stdin.write("3\n")
        process.stdin.flush()
        time.sleep(4)
        # photo
        process.stdin.write("y\n")
        process.stdin.flush()
        time.sleep(4)



        # Ler a saída (se o programa imprime algo)
        while True:
            output = process.stdout.readline()
            if output == "" and process.poll() is not None:
                break
            if output:
                print("Saída:", output.strip())
    except Exception as e:
        print("Erro:", e)
    finally:
        # Garantir que o processo seja encerrado
        process.stdin.close()
        process.stdout.close()
        process.stderr.close()
        process.terminate()



    # move all pictures to the
    #os.system(f"copy {dir_path}build\\Debug\\*.jpg {dir_path}Python_automation\\photos\\")




