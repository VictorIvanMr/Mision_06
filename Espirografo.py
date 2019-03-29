
import pygame   # Librería de pygame
import math
import turtle


# Dimensiones de la pantalla

ANCHO = 1000
ALTO = 1000
p= 9
# Colores

BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad

VERDE = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul

ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul

AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul

NEGRO= (0,0,0) #NEGRO


# Estructura básica de un programa que usa pygame para dibujar

def dibujar(r, R, l):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no



    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente

        # Procesa los eventos que recibe

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir

                termina = True      # Queremos terminar el ciclo



        ventana.fill(NEGRO)
#PONER CODIGO DE DIBUJO APARTIR DE AQUI

        radio = 60

        for angulo in range(0, 400 * (r//math.gcd(r, R)), 1):
            a = math.radians(angulo)
            k = r / R
            x = int(R * ((1 - k) * math.cos(angulo) + l * k * math.cos(((0.5 - k) / k) * angulo)))
            y = int(R * ((1 - k) * math.sin(angulo) - l * k * math.sin(((0.5 - k) / k) * angulo)))
            x1 = int(radio*math.cos(a))
            y1 = int(radio*math.sin(a))

            pygame.draw.circle(ventana, ROJO, (x + ANCHO // 2, ALTO // 2 - y), 1)
            pygame.draw.circle(ventana, AZUL, (x + ANCHO // 2, ALTO // 2 + y), 1)
            pygame.draw.circle(ventana, VERDE, (x * 2 + ANCHO // 2, ALTO // 2 - y), 1)
            pygame.draw.circle(ventana, BLANCO, (x * 2 + ANCHO // 2, ALTO // 2 - 2 * y), 1)
            pygame.draw.circle(ventana, ROJO, (x1 * 2 + ANCHO // 2, ALTO // 2 + 2 * y1), 1)
            pygame.draw.circle(ventana, AZUL, (x1 + ANCHO // 2, ALTO // 2 - y1), 1)
            pygame.draw.circle(ventana, ROJO, (x1 * 4 + ANCHO // 2, ALTO // 2 + 4 * y1), 1)
            #ANILLOS:
            pygame.draw.circle(ventana, BLANCO, (x1 * 2 + ANCHO // 2, ALTO // 2 + 7 * y1), 8)
            pygame.draw.circle(ventana, BLANCO, (x1 * 7 + ANCHO // 2, ALTO // 2 + 2 * y1), 8)
            pygame.draw.circle(ventana, VERDE, (x1 * 2 + ANCHO // 2, ALTO // 2 + 6 * y1), 8)
            pygame.draw.circle(ventana, VERDE, (x1 * 6 + ANCHO // 2, ALTO // 2 + 2 * y1), 8)
            pygame.draw.circle(ventana, ROJO, (x1 * 2 + ANCHO // 2, ALTO // 2 + 8 * y1), 8)
            pygame.draw.circle(ventana, ROJO, (x1 * 8 + ANCHO // 2, ALTO // 2 + 2 * y1), 8)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)

        reloj.tick(5000)  # 40 fps



    # Después del ciclo principal

    pygame.quit()  # termina pygame

# Función principal, aquí resuelves el problema

def main():
    r = 40
    R = 125
    l = 1

    dibujar(r, R ,l)   # Por ahora, solo dibuja



# Llamas a la función principal

main()