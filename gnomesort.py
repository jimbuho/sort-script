import pygame
import basesort
import constants as C

pygame.init()

ventanaAbierta = True
sorted = False

vector = [1,5,6,8,9,192,76,10]

class Gnomesort(basesort.BaseSort):

    def gnome_sort(self, vector):
        n = len(vector)
        index = 0
        while index < n:
            if index == 0:
                index = index + 1
            if vector[index] >= vector[index - 1]:
                index = index + 1
            else:
                vector[index], vector[index-1] = vector[index-1], vector[index]
                index = index - 1
            
            self.show_vector(vector, prioritize=vector[index] if index<n else None)
    
        return vector

sorter = Gnomesort()

while ventanaAbierta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ventanaAbierta = False

    if not sorted:
        sorter.show_text("Ordenamiento por Gnome el Vector:", 
            vector=vector)
        sorter.wait(3)
        sorted_vector = sorter.gnome_sort(vector)
        sorter.show_vector(sorted_vector, C.GREEN)
        sorted = True
    
    pygame.display.update()

pygame.quit()