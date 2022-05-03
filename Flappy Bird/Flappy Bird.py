from ast import Break
import glfw
import sys
from OpenGL.GL import *

from modelo import *
from controlador import Controller

if __name__ == '__main__':

    # Initialize glfw
    if not glfw.init():
        sys.exit()

    width = 960
    height = 540

    window = glfw.create_window(width, height, 'Flappy Kirby', None, None)

    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)

    controlador = Controller()

    # Connecting the callback function 'on_key' to handle keyboard events
    glfw.set_key_callback(window, controlador.on_key)

    # Assembling the shader program (pipeline) with both shaders
    pipeline = es.SimpleTransformShaderProgram()

    # Telling OpenGL to use our shader program
    glUseProgram(pipeline.shaderProgram)

    # Setting up the clear screen color
    glClearColor(0.85, 1, 1, 1)

    # Our shapes here are always fully painted
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    # HACEMOS LOS OBJETOS
    kirby = Kirby(pipeline)
    tubos = Tubo_Creator()
    tubo=Tubo(pipeline)
    suelo=Suelo(pipeline)
    controlador.set_model(kirby)
    controlador.set_eggs(tubos)


    t0 = 0
    espacio_tuberias=0
    while not glfw.window_should_close(window):

        # Calculamos el dt
        ti = glfw.get_time()
        dt = ti - t0
        t0 = ti

        # Using GLFW to check for input events
        glfw.poll_events()  

        # Clearing the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT)


        espacio_tuberias+=1
        if espacio_tuberias%1000==0:
            tubos.create_tubo(pipeline)
        
        tubos.update(0.5 * dt)
        kirby.update(dt)

        kirby.tope() 
        kirby.collide_down(tubos)
        kirby.collide_up(tubos)
        kirby.borrar(tubos)

        # DIBUJAR LOS MODELOS
        kirby.draw(pipeline)
        tubos.draw(pipeline)
        suelo.draw(pipeline)
        
        # Once the render is done, buffers are swapped, showing only the complete scene.
        glfw.swap_buffers(window)

    glfw.terminate()
