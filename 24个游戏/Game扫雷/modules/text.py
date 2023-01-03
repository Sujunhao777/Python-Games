
import pygame


'''文字板'''
class TextBoard(pygame.sprite.Sprite):
    def __init__(self, text, font, position, color, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.font = font
        self.position = position
        self.color = color
    def draw(self, screen):
        text_render = self.font.render(self.text, True, self.color)
        screen.blit(text_render, self.position)
    def update(self, text):
        self.text = text