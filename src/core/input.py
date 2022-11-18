import pygame

class Input:

    def __init__(self):
        # has the user quit the application?
        self.quit = False

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True