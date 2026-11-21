"""
EJERCICIO 1 - PYGAME: "Atrapa las manzanas"
Mueve la canasta con las flechas IZQUIERDA/DERECHA y atrapa las manzanas.
Cada manzana atrapada suma 1 punto; cada una que se cae resta 1 vida.

INSTRUCCIONES: reemplaza cada ____ por el código correcto (hay 13 espacios).
"""
import pygame
import random

# --- Inicialización ---------------------------------------------------------
pygame.init()                                          # 1. Inicia PyGame
ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))      # 2. Crea la ventana
pygame.display.set_caption("Atrapa las manzanas")
reloj = pygame.time.Clock()                            # 3. Reloj para controlar los FPS
fuente = pygame.font.SysFont(None, 36)

# --- Variables del juego ----------------------------------------------------
jugador = pygame.Rect(250, 360, 100, 20)
velocidad_jugador = 7
manzana = pygame.Rect(random.randint(0, ANCHO - 20), 0, 20, 20)
velocidad_manzana = 5                                  # 4. Elige una velocidad de caída (número)
puntos = 0                                             # 5. Puntaje inicial
vidas = 3
nivel = 1

def reiniciar_manzana():
    """Coloca la manzana arriba, en una posición X aleatoria."""
    manzana.x = random.randint(0, ANCHO - manzana.width)
    manzana.y = 0                                      # 6. Arriba de la pantalla


# --- Bucle principal --------------------------------------------------------
corriendo = True
while corriendo:
    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:                 # 7. Evento de cerrar ventana
            corriendo = False

    # Teclado (movimiento continuo)
    teclas = pygame.key.get_pressed()                  # 8. Estado de todas las teclas
    if teclas[pygame.K_LEFT]:                          # 9. Flecha izquierda
        jugador.x -= velocidad_jugador
    if teclas[pygame.K_RIGHT]:
        jugador.x += velocidad_jugador
    jugador.clamp_ip(pantalla.get_rect())                  # Mantiene la canasta dentro de la ventana

    # Lógica
    manzana.y += velocidad_manzana
    if jugador.colliderect(manzana):                   # 10. ¿Hay colisión entre dos Rect?
        puntos +=1
        if puntos >0 and puntos%5 == 0:
            nivel +=1
            velocidad_manzana +=1

            print("velocidad:", velocidad_manzana, "nivel:", nivel)
            

        reiniciar_manzana()
         
    elif manzana.top > ALTO:
        vidas -= 1                                     # 11. Resta una vida
        reiniciar_manzana()
        

    '''if vidas <= 0:
        corriendo = False'''

   
    # Dibujo
    pantalla.fill((20, 20, 40))
    pygame.draw.rect(pantalla, (80, 160, 255), jugador)
    pygame.draw.circle(pantalla, (220, 30, 30), manzana.center, 10)   # 12. Dibuja la manzana
    texto = fuente.render(f"Puntos: {puntos}   Vidas: {vidas}", True, (255, 255, 255))
    
    pantalla.blit(texto, (10, 10))

    if nivel>0:
        if puntos%5 == 0:

            txt_nivel = f"Nivel: {nivel}"

            texto_nivel = fuente.render(txt_nivel, True, (255, 255, 255))            
            w = texto_nivel.get_width()
            h = texto_nivel.get_height()

            pantalla.blit(texto_nivel, (ANCHO/2 -w/2 , ALTO/2 - h/2))
            

    txt_nivel = " "

    if vidas <=0:
        texto_final = fuente.render("GAME OVER", True, (255, 255, 255))            
        w = texto_final.get_width()
        h = texto_final.get_height()

        pantalla.blit(texto_final, (ANCHO/2 -w/2 , ALTO/2 - h/2))

        corriendo = False




    pygame.display.flip()                              # 13. Actualiza la pantalla
    reloj.tick(60)

print(f"Fin del juego. Puntaje final: {puntos}")
pygame.quit()

# --- RETO EXTRA (opcional) ---------------------------------------------------
# a) Haz que la velocidad de la manzana aumente cada 5 puntos.
# b) Muestra "GAME OVER" en pantalla antes de salir.
