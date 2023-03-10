import pygame
import FIRST_PART.PEOPLE.ANNA, FIRST_PART.PEOPLE.KIRA
import FIRST_PART.DATAS.get_datas


class MOVING_PEOPLE:  # сложность в анимации
    def __init__(self):pass

    def anna(self, screen):  # creating animation
        entity_anna = FIRST_PART.PEOPLE.ANNA.setting_entity()
        side = FIRST_PART.DATAS.get_datas

        img = pygame.transform.flip(entity_anna.image, True, False) if side.get_side_user() == 'left\n' \
            else entity_anna.image

        screen.blit(img, entity_anna.rect)

    def kira(self, screen):
        pos = FIRST_PART.PEOPLE.KIRA.get_pos()
        if pos != (0, 0):
            object_kira = FIRST_PART.PEOPLE.KIRA.setting_entity(pos)
            img = pygame.transform.flip(object_kira.image, True, False)

            screen.blit(img, object_kira.rect)
