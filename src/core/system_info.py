from OpenGL.GL import *

def print_system_info():
    print('Vendor: ' + glGetString(GL_VENDOR).decode('utf-8'))
    
    print('Renderer: ' + glGetString(GL_RENDERER).decode('utf-8'))
    
    print("OpenGL version supported: " + glGetString(GL_VERSION).decode('utf-8'))
    
    print(" GLSL version supported: " + glGetString(
        GL_SHADING_LANGUAGE_VERSION).decode('utf-8'))