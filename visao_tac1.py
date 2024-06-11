import cv2
import numpy as np


# global
image_hsv = None
pixel = (20, 60, 80)    # valores atoa

# -----------------------------------------
# começa a procurar rectangulos e de calcular angulos
def Start_Find_Rect():
    init_cam()
    Find_rect()

# para de procurar rectangulos e de calcular angulos
def Stop_Find_Rect():
    release_cap()


# -------------------------------------
# Função para encontrar os limites do hsv
def pick_color(event, x, y, flags, param):
    init_cam()

    # Capturar frame da webcam
    ret, frame = cap.read()

    image_hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)

    while True:
        if event == cv2.EVENT_LBUTTONDOWN:
            pixel = image_hsv[y,x]

            # you might want to adjust the ranges(+-10, etc):
            upper = np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 40])
            lower = np.array([pixel[0] - 10, pixel[1] - 10, pixel[2] - 40])
            print(pixel, lower, upper)
        if event == cv2.EVENT_RBUTTONDOWN:
            break


# ----------------------------------
# Função para encontrar o centro de um retângulo e encontrar o ângulo em relação ao centro
l_frame = 1280/2
max_angle = 52

def centro_retangulo(x, y, w, h):
    centro_x = x + (w // 2)
    centro_y = y + (h // 2)
    if centro_x > l_frame:
        angulo = ((centro_x-l_frame)*max_angle)/l_frame
    elif centro_x < l_frame:
        angulo = max_angle-(centro_x*max_angle)/l_frame
        angulo = 0 - angulo
    else:
        angulo = 0
    print(angulo)
    return centro_x, centro_y

# --------------------------------------------
# função para inicializar a webcam
def init_cam():

    cap = cv2.VideoCapture(0)
    return cap

# ----------------------------------------------
# Inicializar a webcam


init_cam()

# Variável global para armazenar o centro do retângulo sob o cursor do mouse
centro_retangulo_atual = None


# Função de callback para o evento do mouse


# Configurar o callback do mouse
cv2.namedWindow('Frame')


def release_cap():

    # Liberar recursos
    cap.release()
    cv2.destroyAllWindows()

# ---------------------------------
# no futuro recebe como parametro upper e lower para encontrar varias cores

def Find_rect():

    # Capturar frame da webcam
    ret, frame = cap.read()

    largura_janela = 1280
    altura_janela = 750
    imagem_redimensionada = cv2.resize(frame, (largura_janela, altura_janela))

    # Converter frame para espaço de cores HSV
    hsv = cv2.cvtColor(imagem_redimensionada, cv2.COLOR_BGR2HSV)

    # Definir o intervalo de cor magenta (vermelho) em HSV
    lower = np.array([150, 100, 100])
    upper = np.array([179, 255, 255])

    # Criar uma máscara para filtrar apenas a cor azul
    mask = cv2.inRange(hsv, lower, upper)

    # Encontrar contornos na máscara
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Armazenar os retângulos
    retangulos = []

    # Iterar sobre os contornos encontrados
    for contour in contours:
        # Calcular a área do contorno
        area = cv2.contourArea(contour)

        # Se a área for maior que um valor mínimo, consideramos como nosso adesivo
        if area > 1500:
            # Encontrar retângulo delimitador ao redor do adesivo
            x, y, w, h = cv2.boundingRect(contour)

            # Desenhar retângulo ao redor do adesivo
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            centro_retangulo(x, y, w, h)

            # Armazenar o retângulo
            retangulos.append((x, y, w, h))

            # Exibir o frame com o retângulo desenhado
            cv2.imshow('Frame', imagem_redimensionada)

'''
while True:

    global image_hsv, pixel
    cv2.setMouseCallback('hsv', pick_color)

    # Parar o loop quando a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
    release_cap()
'''