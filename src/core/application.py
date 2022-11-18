import pygame
import sys
from core.input import Input


class Application:
    def __init__(self, title='OpenGL', screen_size=[512, 512]):
        # initialize all pygame modules
        pygame.init()
        # indicate rendering details
        display_flags = pygame.DOUBLEBUF | pygame.OPENGL

        # initialize buffers to perform antialiasing
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)

        # use a core OpenGL profile for cross-platform compatibility
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE
        )

        # create and display the window
        self.screen = pygame.display.set_mode(screen_size, display_flags)

        # set the text that appears in the title bar of the window
        pygame.display.set_caption(title)

        # determine if main loop is active
        self.running = True
        
        # manage time-related data and operations
        self.clock = pygame.time.Clock()

        self.input = Input()

    def run(self):
        self.initialize()

        # main loop
        while self.running:
            # process input
            self.input.update()
            if self.input.quit:
                self.running = False

            self.update()

            # render
            pygame.display.flip()

            # pause if necessary to achieve 60 FPS
            self.clock.tick(60)

        # shutdown
        pygame.quit()
        sys.exit()

    # implement by extending class
    def initialize(self):
        pass
    
    # implement by extending class
    def update(self):
        pass
