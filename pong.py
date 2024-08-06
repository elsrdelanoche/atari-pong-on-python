import pygame
import random
import sys
import time

# Inicialización de Pygame
pygame.init()

# Definición de colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
tamaño = (ANCHO, ALTO)
pantalla = pygame.display.set_mode(tamaño)
pygame.display.set_caption("Pong")

# Raquetas y pelota
ancho_raqueta = 15
alto_raqueta = 100
ancho_pelota = 15
alto_pelota = 15

# Posiciones iniciales
x_maquina = 50
y_maquina = (ALTO // 2) - (alto_raqueta // 2)

x_usuario = ANCHO - 50 - ancho_raqueta
y_usuario = (ALTO // 2) - (alto_raqueta // 2)

x_pelota = (ANCHO // 2) - (ancho_pelota // 2)
y_pelota = (ALTO // 2) - (alto_pelota // 2)
vel_pelota_x = random.choice([-5, 5])
vel_pelota_y = random.choice([-5, 5])

# Velocidad de la raqueta de la máquina
velocidad_maquina = 4

# Puntuación
puntuacion_maquina = 0
puntuacion_usuario = 0

# Fuente arcade
fuente = pygame.font.Font("ARCADE_N.TTF", 72)
fuente_pequeña = pygame.font.Font("ARCADE_N.TTF", 28)
fuente_muypequeña = pygame.font.Font("ARCADE_N.TTF", 12)

# Control del tiempo
clock = pygame.time.Clock()

# Variables para el menú
modo_juego = None
seleccionado = "Facil"

# Variable para pausar el juego
pausa = False

def mostrar_texto(texto, fuente, color, x, y):
    imagen = fuente.render(texto, True, color)
    pantalla.blit(imagen, (x, y))

def movimiento_maquina_dificil(y_maquina, y_pelota):
    # Movimiento de la máquina con algo de retardo en la respuesta
    if y_maquina + (alto_raqueta // 2) < y_pelota:
        y_maquina += velocidad_maquina + 1
    elif y_maquina + (alto_raqueta // 2) > y_pelota:
        y_maquina -= velocidad_maquina + 1
    return y_maquina

def movimiento_maquina_facil(y_maquina, y_pelota):
    # Movimiento más simple de la máquina
    if y_maquina + (alto_raqueta // 2) < y_pelota:
        y_maquina += velocidad_maquina
    elif y_maquina + (alto_raqueta // 2) > y_pelota:
        y_maquina -= velocidad_maquina
    return y_maquina

# Bucle del menú de inicio
def mostrar_menu():
    global modo_juego
    global seleccionado
    menu_activo = True

    while menu_activo:
        pantalla.fill(NEGRO)
        mostrar_texto("Pong", fuente, BLANCO, ANCHO // 2 - 140, 125)
        mostrar_texto("Facil", fuente_pequeña, BLANCO, ANCHO // 2 - 70, 275)
        mostrar_texto("Dificil", fuente_pequeña, BLANCO, ANCHO // 2 - 70, 375)
        mostrar_texto("Por: elsrdelanoche", fuente_muypequeña, BLANCO, ANCHO // 2 - 100, 550)
        if seleccionado == "Facil":
            pygame.draw.rect(pantalla, BLANCO, [ANCHO // 2 - 120, 275, 20, 20])
        elif seleccionado == "Dificil":
            pygame.draw.rect(pantalla, BLANCO, [ANCHO // 2 - 120, 375, 20, 20])



        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                    if seleccionado == "Facil":
                        seleccionado = "Dificil"
                    else:
                        seleccionado = "Facil"
                if evento.key == pygame.K_RETURN:
                    modo_juego = seleccionado
                    menu_activo = False

def mostrar_instrucciones():
    instrucciones_activo = True

    while instrucciones_activo:
        pantalla.fill(NEGRO)
        mostrar_texto("Instrucciones:", fuente_pequeña, BLANCO, ANCHO // 2 - 170, 150)
        mostrar_texto("- Centra el puntero a mitad de la pantalla al iniciar", fuente_muypequeña, BLANCO, ANCHO // 2 - 350, 200)
        mostrar_texto("- Mueve el puntero del mouse de arriba a abajo para jugar", fuente_muypequeña, BLANCO, ANCHO // 2 - 350, 225)
        mostrar_texto("- Para pausar el juego presiona la barra ESPACIO", fuente_muypequeña, BLANCO,  ANCHO // 2 - 350, 250)
        mostrar_texto("- Presiona ESC para salir", fuente_muypequeña, BLANCO,  ANCHO // 2 - 350, 275)
        mostrar_texto("<Presiona ENTER para continuar>", fuente_muypequeña, BLANCO,  ANCHO // 2 - 180, 350)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                instrucciones_activo = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Presionar Enter para continuar
                    instrucciones_activo = False


def mostrar_cuenta_regresiva():
    for i in range(3, 0, -1):
        pantalla.fill(NEGRO)
        mostrar_texto(f"Listos en {i}", fuente_pequeña, BLANCO, ANCHO // 2 - 150, ALTO // 2 - 50)
        pygame.display.flip()
        time.sleep(1)

mostrar_menu()
mostrar_instrucciones()
mostrar_cuenta_regresiva()

# Bucle principal del juego
hecho = False
while not hecho:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                pausa = not pausa
            if evento.key == pygame.K_ESCAPE:
                hecho = True

    if not pausa:
        # Movimiento de la raqueta del usuario con el mouse
        _, y_mouse = pygame.mouse.get_pos()
        y_usuario = y_mouse - (alto_raqueta // 2)

        # Movimiento de la raqueta de la máquina
        if modo_juego == "Facil":
            y_maquina = movimiento_maquina_facil(y_maquina, y_pelota)
        elif modo_juego == "Dificil":
            y_maquina = movimiento_maquina_dificil(y_maquina, y_pelota)

        # Movimiento de la pelota
        x_pelota += vel_pelota_x
        y_pelota += vel_pelota_y

        # Rebote de la pelota en los bordes superiores e inferiores
        if y_pelota <= 0 or y_pelota >= ALTO - alto_pelota:
            vel_pelota_y *= -1

        # Rebote de la pelota en las raquetas
        if (x_pelota <= x_maquina + ancho_raqueta and
            y_pelota + alto_pelota >= y_maquina and
            y_pelota <= y_maquina + alto_raqueta):
            vel_pelota_x *= -1

        if (x_pelota >= x_usuario - ancho_pelota and
            y_pelota + alto_pelota >= y_usuario and
            y_pelota <= y_usuario + alto_raqueta):
            vel_pelota_x *= -1

        # Puntuación y reinicio de la pelota si sale de los límites
        if x_pelota <= 0:
            puntuacion_usuario += 1
            x_pelota = (ANCHO // 2) - (ancho_pelota // 2)
            y_pelota = (ALTO // 2) - (alto_pelota // 2)
            vel_pelota_x = random.choice([-5, 5])
            vel_pelota_y = random.choice([-5, 5])

        if x_pelota >= ANCHO - ancho_pelota:
            puntuacion_maquina += 1
            x_pelota = (ANCHO // 2) - (ancho_pelota // 2)
            y_pelota = (ALTO // 2) - (alto_pelota // 2)
            vel_pelota_x = random.choice([-5, 5])
            vel_pelota_y = random.choice([-5, 5])

        # Dibujado en pantalla
        pantalla.fill(NEGRO)
        pygame.draw.rect(pantalla, BLANCO, [x_maquina, y_maquina, ancho_raqueta, alto_raqueta])
        pygame.draw.rect(pantalla, BLANCO, [x_usuario, y_usuario, ancho_raqueta, alto_raqueta])
        pygame.draw.rect(pantalla, BLANCO, [x_pelota, y_pelota, ancho_pelota, alto_pelota])

        # Dibujar la línea punteada en el centro
        for i in range(0, ALTO, 20):
            pygame.draw.line(pantalla, BLANCO, (ANCHO // 2, i), (ANCHO // 2, i + 10))

        # Mostrar la puntuación y etiquetas
        mostrar_texto("Maquina", fuente_pequeña, BLANCO, ANCHO // 4 - 90, 10)
        mostrar_texto("Jugador", fuente_pequeña, BLANCO, 3 * ANCHO // 4 - 90, 10)
        texto_maquina = fuente.render(str(puntuacion_maquina), True, BLANCO)
        pantalla.blit(texto_maquina, (ANCHO // 4 - 20, 40))
        texto_usuario = fuente.render(str(puntuacion_usuario), True, BLANCO)
        pantalla.blit(texto_usuario, (3 * ANCHO // 4 - 20, 40))

    # Actualización de la pantalla
    pygame.display.flip()

    # Control de la velocidad de juego
    clock.tick(60)

# Salida de Pygame
pygame.quit()
