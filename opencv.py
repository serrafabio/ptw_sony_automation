## PUT THIS ALL IN ONE CELL!
import cv2

def listar_cameras():
    index = 0
    print("Procurando dispositivos de câmera...")
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.isOpened():
            break
        print(f"Câmera disponível no índice: {index}")
        cap.release()
        index += 1

    if index == 0:
        print("Nenhuma câmera detectada.")

listar_cameras()

cap = cv2.VideoCapture(2)  # Use 0 para a câmera padrão

if not cap.isOpened():
    print("Erro ao acessar a câmera.")
    exit()
while True:
    # Captura um único frame
    ret, frame = cap.read()
    if ret:
        # Exibe a imagem capturada
        cv2.imshow('Imagem Colorida', frame)
    else:
        print("Erro ao capturar a imagem.")

    # This command let's us quit with the "q" button on a keyboard.
    # Simply pressing X on the window won't work!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha as janelas
cap.release()
cv2.destroyAllWindows()