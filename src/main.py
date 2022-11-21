from core.application import Application
from core.shader import Shader
from core.vertex_array import VertexArray
from core.system_info import print_system_info
from OpenGL.GL import *

class Test(Application):

    def initialize(self):
        shader = Shader('./shaders/basicVertShader.glsl', './shaders/basicFragShader.glsl')
        vao = VertexArray()
        glPointSize(10)
        shader.use()

    def update(self):
        glDrawArrays(GL_POINTS, 0, 1)
        




Test().run()