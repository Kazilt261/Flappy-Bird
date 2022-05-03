"""
Clase controlador, obtiene el input, lo procesa, y manda los mensajes
a los modelos.
"""

from modelo import Kirby, Tubo_Creator
import glfw
import sys
from typing import Optional


class Controller(object):
    model: Optional['Kirby'] 
    eggs: Optional['Tubo_Creator']

    def __init__(self):
        self.model = None
        self.eggs = None

    def set_model(self, m):
        self.model = m

    def set_eggs(self, e):
        self.eggs = e

    def on_key(self, window, key, scancode, action, mods):
        if not (action == glfw.PRESS or action == glfw.RELEASE):  # Particular de la app
            return
        if key == glfw.KEY_ESCAPE:
            glfw.terminate()
            sys.exit()

        # Le pasa los eventos a los modelos
        elif key == glfw.KEY_UP and action == glfw.PRESS:
            self.model.volar()
