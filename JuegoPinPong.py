import pygame
from pygame.locals import*
import random

winHorizontal = 800 #tamaño de la ventana horizontal
winVertical = 600 #tamaño de la ventana vertical
fps=60
white=(255, 255, 255)
black=(0,0,0,)

class pelotaP:
        def __init__(self, fichero_imagen):
            self.imagen=pygame.image.load(fichero_imagen).convert_alpha()
            self.ancho, self.alto = self.imagen.get_size()
            self.x = winHorizontal/2-self.ancho/2
            self.y=winVertical/2-self.alto/2
            self.dir_x=random.choice([-5,5])
            self.dir_y=random.choice([-5,5])
            self.puntuacion_jug=0    #puntaje para el jugador
            self.puntuacion_IA=0 #puntaje para la IA
        def movimiento(self):
            self.x+=self.dir_x
            self.y+=self.dir_y
        def reiniciar(self):     #volver la pelota a en medio de la ventana
            self.x=winHorizontal/2-self.ancho/2
            self.y=winVertical/2-self.alto/2
            self.dir_x=-self.dir_x
            self.dir_y=random.choice([-5,5])
        def rebotar(self):
            if self.x<=-self.ancho:
               self.puntuacion_IA+=1
            if self.x >=winHorizontal:
                self.reiniciar()
                self.puntuacion_jug+=1
            if self.y>=0:
                self.dir_y=-self.dir_y
            if self.y+self.alto>=winVertical:
                self.dir_y=-self.dir_y

class raqueta:
    def __init__(self):
        self.imagen=pygame.image.load("raqueta.png").convert_alpha()
        self.ancho,self.alto=self.imagen.get_size()
        self.x=0
        self.y=winVertical/2-self.alto/2
        self.dir_y=0
    def movimiento(self):  #movimiento de la raqueta de los dos jugadores
        self.y+=self.dir_y
        if self.y<=0:
            self.y=0
        if self.y+self.alto>=winVertical:
            self.y=winVertical-self.alto
    def movimiento_IA(self):
        if self.y>pelota.y:
            self.dir_y=-3
        elif self.y<pelota.y:
            self.dir_y=+3
        else:
            self.dir_y=0
        self.y+=self.dir_y
    def golpear(self, pelota):
        if(
            pelota.x<self.x+self.ancho
            and pelota.x>self.x 
            and pelota.y+pelota.alto>self.y
            and pelota.y>self.y+self.alto
        ):
          pelota.dir_x=-pelota.dir_x
          pelota.x=self.x+self.ancho
          



