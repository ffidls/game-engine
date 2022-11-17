import pygame
import DIALOG_BUTTONS.mechanic_contact
import DATAS.get_datas, DATAS.const


class ASSEMBLING:
    def __init__(self):
        self.img_button = pygame.image.load(DATAS.get_datas.img_button())
        self.inf_button_dialog = DIALOG_BUTTONS.mechanic_contact.SETTING_CONTACT()

        self.window_dialog = pygame.image.load(DATAS.get_datas.window_dialog())

    def draw_button(self, SCREEN):
        pos = self.inf_button_dialog.setting_for_draw_button()
        SCREEN.blit(self.img_button, (pos[0], pos[1]))

    def draw_dialog(self, SCREEN):
        datas_dialog = self.inf_button_dialog.datas_from_draw_dialog()
        if datas_dialog is not None:
            human, phrase = datas_dialog[1], datas_dialog[2]
            SCREEN.blit(self.window_dialog, DATAS.const.POS_DIALOG_WINDOW)

    def result(self, SCREEN):
        contact_with_button = DATAS.get_datas.inf_for_button()[0]
        self.draw_button(SCREEN) if contact_with_button else None
        self.draw_dialog(SCREEN)
