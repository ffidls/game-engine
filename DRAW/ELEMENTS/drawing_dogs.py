import pygame

import DATAS.possions
import DOG.description_dogs


class MOVING_DOG:  # сложность в анимации
    def __init__(self):
        self.datas_Miki = DOG.description_dogs.DOG()

    def miki(self, screen):  # creating animation
        '''        start_pos_zona = DATAS.possions.give_pos_zona()
        entity_zona = pygame.Rect(start_pos_zona[1], start_pos_zona[0], 150, 150)
        pygame.draw.rect(screen, (112, 15, 105), entity_zona)'''

        pos = DATAS.possions.give_pos_miki()
        entity_miki = pygame.Rect(pos[1], pos[0], 20, 20)
        pygame.draw.rect(screen, (24, 125, 55), entity_miki)

    def kira(self):
        pass
