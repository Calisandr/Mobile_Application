import pygame
import sys

from pygame import draw, KEYDOWN, K_w, K_s, K_SPACE

pygame.init()

bg = pygame.image.load("фон.jpg")
screen  = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)
pygame.display.set_caption("Mathematical Simulator")
img = pygame.image.load("логотип.jpg")
pygame.display.set_icon(img)
font = pygame.font.SysFont("Codec Pro Ultra", 60)
white = (255, 255, 255)

class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0

    def append_option(self, option, callback):
        self._option_surfaces.append(font.render(option, True, (white)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surfaces) - 1))

    def select(self):
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (500, 450 + i * 110)
            if i == self._current_option_index:
                draw.rect(surf, (0, 206, 209), option_rect)
            surf.blit(option, option_rect)

menu = Menu()
menu.append_option("PLAY", lambda: print("PLAY"))
menu.append_option("QUIT", quit)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_w:
                menu.switch(-1)
            elif event.key == K_s:
                menu.switch(1)
            elif event.key == K_SPACE:
                menu.select()
            
    pygame.display.flip()
    screen.blit(bg, (0, 0))
    menu.draw(screen, 100, 100, 75)
    pygame.display.update()