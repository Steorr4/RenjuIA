import pygame


class Text:
    def __init__(self, text: str, pos: (int, int), size: int = 26, color=(0, 0, 0)):
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = size
        self.fontcolor = color

        self.set_font()
        self.render()

    def set_font(self):
        self.font = pygame.font.Font("./game/assets/ps2p.ttf", self.fontsize)

    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
