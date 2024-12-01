import subprocess
import time
import threading
import queue

# Asynchronous function foŕ the stdout
def enqueue_output(out, queue):
    for line in iter(out.readline, ''):
        queue.put(line)
    out.close()

dir_path = r"C:\\Users\\serra\\OneDrive\\Documentos\\WiP\\HiWi\\Alex\\build\\Debug\\RemoteCli.exe"

# Inicia o subprocesso
process = subprocess.Popen(
    [dir_path],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1  # Linha a linha
)

# Fila para armazenar saídas
stdout_queue = queue.Queue()
stderr_queue = queue.Queue()

# Threads para leitura assíncrona
stdout_thread = threading.Thread(target=enqueue_output, args=(process.stdout, stdout_queue))
stderr_thread = threading.Thread(target=enqueue_output, args=(process.stderr, stderr_queue))
stdout_thread.start()
stderr_thread.start()

try:
    # Enviar comandos para o subprocesso
    # Setting ISO
    commands = ["1\n", "1\n", "3\n", "10\n", "y\n", "14\n", '0\n', '0\n', 'x\n']
    # Setting Shutter speed
    commands = ["1\n", "1\n", "3\n", "2\n", "y\n", "20\n", '0\n', '0\n', 'x\n']
    # Aperture
    #commands = ["1\n", "1\n", "3\n", "1\n", "y\n", "14\n", '0\n', '0\n', 'x\n']
    for command in commands:
        process.stdin.write(command)
        process.stdin.flush()

        # Aguardar resposta ou dar tempo para o subprocesso processar
        time.sleep(2)

        # Imprimir as mensagens do subprocesso
        while not stdout_queue.empty():
            print("STDOUT:", stdout_queue.get_nowait().strip())
        while not stderr_queue.empty():
            print("STDERR:", stderr_queue.get_nowait().strip())
except Exception as e:
    print(f"Erro ao interagir com o processo: {e}")
finally:
    # Fechar stdin e esperar o subprocesso terminar
    process.stdin.close()
    process.wait()
    stdout_thread.join()
    stderr_thread.join()