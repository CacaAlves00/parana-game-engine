from OpenGL.GL import *

class Shader:
    def __init__(self, vertexShaderCodePath, fragmentShaderCodePath):
        self.__vertexShaderRef = self.__create_shader(vertexShaderCodePath,
        GL_VERTEX_SHADER)
        self.__fragmentShaderRef = self.__create_shader(fragmentShaderCodePath,
        GL_FRAGMENT_SHADER)

        self.__compile(self.__vertexShaderRef)
        self.__compile(self.__fragmentShaderRef)

        self.__create_program()

        self.__link_program()

    def __create_shader(self, shader_code_path, shader_type):
        shader_code = self.__get_shader_code(shader_code_path)

        # specify required OpenGL/GLSL version
        shader_code = '#version 330\n' + shader_code

        # create empty shader object and return reference value
        shader_ref = glCreateShader(shader_type)
        
        # stores the source code in the shader
        glShaderSource(shader_ref, shader_code)

        return shader_ref

    def __get_shader_code(self, shader_code_path):
        shader_code = ''
        with open(shader_code_path) as f:
            shader_code_arr = f.readlines()

            for item in shader_code_arr:
                shader_code += item
        
        return shader_code

    def __compile(self, shader_ref):
        # compiles source code previously stored in the shader object
        glCompileShader(shader_ref)

        # queries whether shader compile was successful
        compile_success = glGetShaderiv(shader_ref, GL_COMPILE_STATUS)

        if not compile_success:
            # retrieve error message
            error_message = glGetShaderInfoLog(shader_ref)
            # free memory used to store shader program
            glDeleteShader(shader_ref)
            # convert byte string to character string
            error_message = '\n' + error_message.decode('utf-8')
            # raise exception: halt program and print error message
            raise Exception( error_message )

    def __create_program(self):
        # create empty program object and store reference to it
        self.__program_ref = glCreateProgram()

        # attach previously compiled shader programs
        glAttachShader(self.__program_ref, self.__vertexShaderRef)
        glAttachShader(self.__program_ref, self.__fragmentShaderRef)

        self.__link_program()

    def __link_program(self):
        # link vertex shader to fragment shader
        glLinkProgram(self.__program_ref)

        # queries whether program link was successful
        link_success = glGetProgramiv(self.__program_ref,
        GL_LINK_STATUS)

        if not link_success:
            # retrieve error message
            error_message = glGetProgramInfoLog(self.__program_ref)
            # free memory used to store program
            glDeleteProgram(self.__program_ref)
            # convert byte string to character string
            error_message = '\n' + error_message
            # raise exception: halt application and print error message
            raise Exception(error_message)

    def use(self):
        glUseProgram(self.__program_ref)