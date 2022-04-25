import pygame
import time
import constants as C

pygame.init()

class BaseSort:

    def __init__(self):
        self.font = pygame.font.SysFont(None, C.FONT_SIZE)
        self.big_font = pygame.font.SysFont(None, C.BIGFONT_SIZE)
        self.screen = pygame.display.set_mode([C.WIDTH,C.HEIGHT])

    def clean_screen(self):
        self.screen.fill((0,0,0))
        pygame.display.flip()

    def show_vector(self, vector, background=C.WHITE, prioritize=None, update=True):
        x = (C.WIDTH/2) - len(vector)/2 * (C.RADIO * 2)
        index = 0

        if update:
            self.clean_screen()

        for item in vector:
            if prioritize and prioritize == item:
                self.draw_node(x + (C.RADIO*2)*index, (C.HEIGHT-C.RADIO)/2, 
                    str(item), C.BLUE)
            else:
                self.draw_node(x + (C.RADIO*2)*index, (C.HEIGHT-C.RADIO)/2, 
                    str(item), background)
            index += 1

        if update:
            pygame.display.update()
            self.wait(C.TIMEWAIT)

    def draw_node(self, x, y, text, color=C.WHITE):
        pygame.draw.circle(self.screen, color, [x, y], C.RADIO)    
        font_color = C.RED if color == C.WHITE else C.WHITE
        text_obj = self.font.render(text, True, font_color)
        self.screen.blit(text_obj, text_obj.get_rect(center = (x, y)))

    def show_text(self, text, font_color=C.WHITE, vector=None):
        self.clean_screen()

        text_obj = self.big_font.render(text, True, font_color)
        
        self.screen.blit(text_obj, text_obj.get_rect(center = 
            ((C.WIDTH - len(text))/2, 60)))

        if vector:
            self.show_vector(vector, update=False)

        pygame.display.update()

    def wait(self,seconds):
        time.sleep(seconds)
