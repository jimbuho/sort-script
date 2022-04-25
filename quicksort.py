import pygame
import time
import basesort
import constants as C

pygame.init()

ventanaAbierta = True
sorted = False

vector = [1,5,6,8,9,192,76,6]

class Quicksort(basesort.BaseSort):

    def quick_sort(self, vector):
        if not vector:
            return []
        else:
            pivote = vector[-1]
            menor = [x for x in vector if x <  pivote]
            mas_grande = [x for x in vector[:-1] if x >= pivote]
            response = self.quick_sort(menor) + [pivote] + self.quick_sort(mas_grande)

            self.show_vector(response, prioritize=pivote)

            return response

sorter = Quicksort()

while ventanaAbierta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ventanaAbierta = False

    if not sorted:
        sorter.show_text("Ordenamiento por Quicksort el Vector (Pivot Azul):", 
            vector=vector)
        sorter.wait(4)
        sorted_vector = sorter.quick_sort(vector)
        sorter.show_vector(sorted_vector, C.GREEN)
        sorted = True
    
    pygame.display.update()

pygame.quit()