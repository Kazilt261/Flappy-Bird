"""
Este archivo generaría todos los modelos que tiene la aplicación. En programas más complicados
tendríamos una cosa así:

src/models/actor/chansey.py
src/models/actor/egg.py
src/models/factory/eggcreator.py

...
Y este archivo sería algo como
src/models/model.py --> sólo importaría los objetos que usa el resto de la aplicación, sin tocar el detalle mismo

from src.models.actor.chansey import Chansey
from src.models.actor.factory import EggCreator
...

Pero aquí, como nuestra app es sencilla, definimos todas las clases aquí mismo.
1. Chansey
2. Los huevos
"""

import grafica.transformations as tr
import grafica.basic_shapes as bs
import grafica.scene_graph as sg
import grafica.easy_shaders as es

from OpenGL.GL import glClearColor, GL_STATIC_DRAW
import random
from typing import List


def create_gpu(shape, pipeline):
    gpu = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpu)
    gpu.fillBuffers(shape.vertices, shape.indices, GL_STATIC_DRAW)
    return gpu


class Kirby(object):

    def __init__(self, pipeline):
        # Figuras básicas
        gpu_body_quad = create_gpu(bs.createColorQuad(0.99, 0.65, 0.91), pipeline)  # rosado
        gpu_leg_quad = create_gpu(bs.createColorQuad(0.9, 0.19, 0.18), pipeline)  # rosado fuerte
        gpu_eye_quad = create_gpu(bs.createColorQuad(1, 1, 1), pipeline)  # blanco
        gpu_punto_quad = create_gpu(bs.createColorQuad(0, 0, 0), pipeline)

        body = sg.SceneGraphNode('body')
        body.transform = tr.scale(0.7,1.4,1)
        body.childs += [gpu_body_quad]

        # Creamos las piernas
        leg = sg.SceneGraphNode('leg')  # pierna generica
        leg.transform = tr.scale(0.36, 0.7, 1)
        leg.childs += [gpu_leg_quad]

        # Izquierda
        leg_izq = sg.SceneGraphNode('legLeft')
        leg_izq.transform = tr.translate(-0.5, -0.5, 0)  # tr.matmul([])..
        leg_izq.childs += [leg]

        

        # Ojitos
        eye = sg.SceneGraphNode('eye')
        eye.transform = tr.scale(0.25, 0.25, 1)
        eye.childs += [gpu_eye_quad]

        punton = sg.SceneGraphNode('eye')
        punton.transform = tr.scale(0.1, 0.1, 1)
        punton.childs += [gpu_punto_quad]
        punto= sg.SceneGraphNode('eyeRight')
        punto.transform = tr.translate(0.17, 0.45, 0)
        punto.childs += [punton]

        eye_der = sg.SceneGraphNode('eyeRight')
        eye_der.transform = tr.translate(0.1, 0.4, 0)
        eye_der.childs += [eye]

        # Ensamblamos el mono
        mono = sg.SceneGraphNode('chansey')
        mono.transform = tr.matmul([tr.scale(0.1, 0.1, 0), tr.translate(0, 0, 0)])
        mono.childs += [body, leg_izq, eye_der,punto]

        transform_mono = sg.SceneGraphNode('chanseyTR')
        transform_mono.childs += [mono]

        self.model = transform_mono
          # -1, 0, 1
          # Variable que indica la posicion visual de chansey (-0.7, 0.7)
        self.alive = True
        self.pos_y = 0.5
        
    def volar(self):
        if not self.alive:
            return
        self.pos_y += 0.25
        
    def draw(self, pipeline):
        self.model.transform = tr.translate(0, self.pos_y, 0)
        sg.drawSceneGraphNode(self.model, pipeline, "transform")
    def update(self, dt):
        if not self.alive:
            return
        self.pos_y -= 0.7*dt

    def die(self):  # DARK SOULS
        glClearColor(1, 0, 0, 1)  # Cambiamos a rojo

        self.on = False
    def tope(self):
        if self.alive==False:
            return
        else:
            if self.pos_y < -0.7:
                  # YOU D   I   E   D, GIT GUD
                print('MUERE, GIT GUD')
                self.die()
                self.alive = False
            elif self.pos_y>1:
                print('MUERE, GIT GUD')
                self.die()
                self.alive=False
        
                
                

    def modifymodel(self):
        # Transforma la geometria del modelo segun las variables internas
        # Podria ser una funcion hiper gigante
        self.model.transform = tr.translate(0, self.y, 0)
    def collide_up(self, tubos: 'Tubo_Creator'):
        if not tubos.on:  # Si el jugador perdió, no detecta colisiones
            return
        deleted_tubos = []

        for e in tubos.tubos:
            if self.alive==False:
                return
            else:
                if e.pos_y==1:
                    if -0.4<e.pos_x<-0.1 and self.pos_y+1>(e.pos_y+0.31):
                        print('MUERE, GIT GUD')  # YOU D   I   E   D, GIT GUD
                        tubos.die()  # Básicamente cambia el color del fondo, pero podría ser algo más elaborado, obviamente
                        self.alive = False
                if e.pos_y==0.75:
                    if -0.4<e.pos_x<-0.1 and self.pos_y+1>(e.pos_y+0.38):
                        print('MUERE, GIT GUD')  # YOU D   I   E   D, GIT GUD
                        tubos.die()  # Básicamente cambia el color del fondo, pero podría ser algo más elaborado, obviamente
                        self.alive = False
                if e.pos_y==1.25:
                    if -0.4<e.pos_x<-0.1 and self.pos_y+1>(e.pos_y+0.24):
                        print('MUERE, GIT GUD')  # YOU D   I   E   D, GIT GUD
                        tubos.die()  # Básicamente cambia el color del fondo, pero podría ser algo más elaborado, obviamente
                        self.alive = False
                if e.pos_y==1.5:
                    if -0.4<e.pos_x<-0.1 and self.pos_y+1>(e.pos_y+0.16):
                        print('MUERE, GIT GUD')  # YOU D   I   E   D, GIT GUD
                        tubos.die()  # Básicamente cambia el color del fondo, pero podría ser algo más elaborado, obviamente
                        self.alive = False
                if e.pos_y==1.75:
                    if -0.4<e.pos_x<-0.1 and self.pos_y+1>(e.pos_y+0.1):
                        print('MUERE, GIT GUD')  # YOU D   I   E   D, GIT GUD
                        tubos.die()  # Básicamente cambia el color del fondo, pero podría ser algo más elaborado, obviamente
                        self.alive = False


    def collide_down(self, tubos: 'Tubo_Creator'):
        if not tubos.on:  # Si el jugador perdió, no detecta colisiones
            return
        deleted_tubos = []

        for e in tubos.tubos:
            if self.alive==False:
                return
            else:    
                if e.pos_y==1:
                    if -0.4<e.pos_x<-0.1 and (e.pos_y-0.31)>(self.pos_y+1):
                        print('MUERE, GIT GUD')  # YOU D   I   E   D, GIT GUD
                        tubos.die()  # Básicamente cambia el color del fondo, pero podría ser algo más elaborado, obviamente
                        self.alive = False
                if e.pos_y==0.75:
                    if -0.4<e.pos_x<-0.1 and (e.pos_y-0.25)>(self.pos_y+1):
                        print('MUERE, GIT GUD')  # YOU D   I   E   D, GIT GUD
                        tubos.die()  # Básicamente cambia el color del fondo, pero podría ser algo más elaborado, obviamente
                        self.alive = False
                if e.pos_y==1.25:
                    if -0.4<e.pos_x<-0.1 and (e.pos_y-0.4)>(self.pos_y+1):
                        print('MUERE, GIT GUD')  # YOU D   I   E   D, GIT GUD
                        tubos.die()  # Básicamente cambia el color del fondo, pero podría ser algo más elaborado, obviamente
                        self.alive = False
                if e.pos_y==1.5:
                    if -0.4<e.pos_x<-0.1 and (e.pos_y-0.47)>(self.pos_y+1):
                        print('MUERE, GIT GUD')  # YOU D   I   E   D, GIT GUD
                        tubos.die()  # Básicamente cambia el color del fondo, pero podría ser algo más elaborado, obviamente
                        self.alive = False
                if e.pos_y==1.75:
                    if -0.4<e.pos_x<-0.1 and (e.pos_y-0.55)>(self.pos_y+1):
                        print('MUERE, GIT GUD')  # YOU D   I   E   D, GIT GUD
                        tubos.die()  # Básicamente cambia el color del fondo, pero podría ser algo más elaborado, obviamente
                        self.alive = False
                
    def borrar(self,tubos:'Tubo_Creator'):
        if not tubos.on:  
            return
        deleted_tubos = []
        for e in tubos.tubos:
            if e.pos_x<-1.3:
                deleted_tubos.append(e)
        tubos.delete(deleted_tubos)
    

class Suelo(object):
    def __init__(self,pipeline):
        gpu_suelo=create_gpu(bs.createColorQuad(0.84,0.65,0.29),pipeline)
        gpu_pasto=create_gpu(bs.createColorQuad(0.45,0.74,0.18),pipeline)
        suelo=sg.SceneGraphNode('suelo')
        suelo.transform=tr.translate(0,-0.6,1)
        suelo.childs+=[gpu_suelo]
        pasto=sg.SceneGraphNode('pasto')
        pasto.transform=tr.translate(0,0.1,1)
        pasto.childs+=[gpu_pasto]
        suelo_tr=sg.SceneGraphNode('sueloTR')
        suelo_tr.childs+=[suelo]
        pasto_tr=sg.SceneGraphNode('pastoTR')
        pasto_tr.childs+=[pasto]


        mono = sg.SceneGraphNode('chansey')
        mono.transform = tr.matmul([tr.scale(2, 0.2, 0), tr.translate(0, 0.5, 0)])
        mono.childs += [pasto,suelo]
        transform_mono = sg.SceneGraphNode('pisoTR')
        transform_mono.childs += [mono]
        self.pos_y=-1
        self.pos_x=0
        self.model=transform_mono



    def draw(self, pipeline):
        self.model.transform = tr.translate(0.7 * self.pos_x, self.pos_y, 0)
        sg.drawSceneGraphNode(self.model, pipeline, "transform")




    

class Tubo(object):
    
    def __init__(self, pipeline):
        gpu_tubo = create_gpu(bs.createColorQuad(0.13, 0.7, 0.3), pipeline)
        
        tubo = sg.SceneGraphNode('leg')  # pierna generica
        tubo.transform = tr.scale(0.25,1.2, 1)
        tubo.childs += [gpu_tubo]

        # Izquierda
        tubo_up = sg.SceneGraphNode('tuboUp')
        tubo_up.transform = tr.translate(0.5, 1, 0)  # tr.matmul([])..
        tubo_up.childs += [tubo]

        tubo_down = sg.SceneGraphNode('tuboDown')
        tubo_down.transform = tr.translate(0.5, -1, 0)
        tubo_down.childs += [tubo]
        
        mono = sg.SceneGraphNode('Tuberia')
        mono.transform = tr.matmul([tr.scale(0.5, 1, 0), tr.translate(0, -0.7, 0)])
        mono.childs += [tubo_down, tubo_up]
        transform_mono = sg.SceneGraphNode('TuberiaTR')
        transform_mono.childs += [mono]
        self.pos_y=random.choice([0.75,1,1.25,1.5,1.75])
        self.pos_x = 1  
        self.model = transform_mono

    def draw(self, pipeline):
        self.model.transform = tr.translate(self.pos_x, 0.7*self.pos_y, 0)
        sg.drawSceneGraphNode(self.model, pipeline, "transform")

    def update(self, dt):
        self.pos_x -= dt
    
    
class Tubo_Creator(object):
    tubos: List['Tubo']

    def __init__(self):
        self.tubos = []
        self.on = True

    def die(self):  # DARK SOULS
        glClearColor(1, 0, 0, 1.0)  # Cambiamos a rojo
        self.on = False  # Dejamos de generar huevos, si es True es porque el jugador ya perdió
    
    def create_tubo(self, pipeline):
            self.tubos.append(Tubo(pipeline))

    def draw(self, pipeline):
        for k in self.tubos:
            k.draw(pipeline)

    def update(self, dt):
        for k in self.tubos:
            k.update(dt)

    def delete(self, d):
        if len(d) == 0:
            return
        remain_tubos = []
        for k in self.tubos:  # Recorro todos los huevos
            if k not in d:  # Si no se elimina, lo añado a la lista de huevos que quedan
                remain_tubos.append(k)
        self.tubos = remain_tubos  # Actualizo la lista
