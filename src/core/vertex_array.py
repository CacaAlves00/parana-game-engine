from OpenGL.GL import *

class VertexArray:
    def __init__(self, vaoCount=1):
        self.__vaoRef = glGenVertexArrays(vaoCount)
        
        self.bind()

    def bind(self):
        glBindVertexArray(self.__vaoRef)