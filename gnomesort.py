import pygame
import time

pygame.init()

WIDTH = 800
HEIGHT = 600
RADIO = 20

WHITE = [255,255,255]
GREEN = [0,150,0]
RED = [255,0,0]
BLUE = [0,0,200]

TIMEWAIT = 1

font = pygame.font.SysFont(None, 20)

BIGFONT_SIZE = 30

big_font = pygame.font.SysFont(None, BIGFONT_SIZE)

screen = pygame.display.set_mode([WIDTH,HEIGHT])

def clean_screen():
    screen.fill((0,0,0))
    pygame.display.flip()

def show_vector(vector, background=WHITE, prioritize=None):
    x = (WIDTH/2) - len(vector)/2 * (RADIO * 2)
    index = 0
    clean_screen()

    for item in vector:
        if prioritize and prioritize == item:
            draw_node(x + (RADIO*2)*index, (HEIGHT-RADIO)/2, str(item), BLUE)
        else:
            draw_node(x + (RADIO*2)*index, (HEIGHT-RADIO)/2, str(item), background)
        index += 1

    pygame.display.update()
    time.sleep(TIMEWAIT)

def draw_node(x, y, text, color=WHITE):
    pygame.draw.circle(screen, color, [x, y], RADIO)    
    font_color = RED if color == WHITE else WHITE
    text_obj = font.render(text, True, font_color)
    screen.blit(text_obj, text_obj.get_rect(center = (x, y)))

def show_text(text, font_color=WHITE, vector=None):
    clean_screen()
    x = (WIDTH - len(text))/2
    y = 60
    text_obj = big_font.render(text, True, font_color)
    screen.blit(text_obj, text_obj.get_rect(center = (x, y)))
    
    if vector:
        x = (WIDTH/2) - len(vector)/2 * (RADIO * 2)
        index = 0

        for item in vector:
            draw_node(x + (RADIO*2)*index, (HEIGHT-RADIO)/2, str(item), WHITE)
            index += 1

    pygame.display.update()

def quick_sort(vector):
    if not vector:
        return []
    else:
        pivote = vector[-1]
        menor = [x for x in vector if x <  pivote]
        mas_grande = [x for x in vector[:-1] if x >= pivote]
        response = quick_sort(menor) + [pivote] + quick_sort(mas_grande)

        show_vector(response, prioritize=pivote)

        return response

ventanaAbierta = True
sorted = False

vector = [1,5,6,8,9,2]

while ventanaAbierta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ventanaAbierta = False

    if not sorted:
        show_text("Ordenamiento por Quicksort el Vector (Pivot Azul):", vector=vector)
        time.sleep(TIMEWAIT*4)
        quick_sort(vector)
        show_vector(vector, GREEN)
        sorted = True
    
    pygame.display.update()

pygame.quit()