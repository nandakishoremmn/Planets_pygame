'''
Created on 30-May-2012

@author: NANDU
'''
from initialise import screen
from pygame import image
from math import ceil
from random import random, randrange, randint
from gameobjects.vector2 import Vector2



class PLANET:
    
    def __init__(self,position=Vector2(0,0),velocity=Vector2(0,0)):
        self.pic = image.load('images/planet.png')
        self.size  = Vector2(self.pic.get_width(),self.pic.get_height())
        x = ( screen.get_width()*.3 + random()*screen.get_width()*.4 )
        y = ( screen.get_height()*.4 + random()*screen.get_height()*.2 )
        dx = (randrange(-100,100)*0.01)
        dy = (randrange(-100,100)*0.01)
        self.position = position if position else Vector2(float(x),float(y))
        self.position_int = Vector2(0,0)
        self.velocity = velocity if  velocity else Vector2(dx,dy)
        if randint(0,1):
            self.mass = randint(1,10)
        else:
            self.mass = randint(20,30)
            self.velocity/=1.0
          
    def update_velocity(self,acceleration): 
        self.velocity += acceleration  
        
    def update_position(self):
        self.position += self.velocity
        
    def reverse(self):
        self.velocity = -self.velocity
            
    def draw(self):
        self.position_int.x,self.position_int.y = int(self.position.x),int(self.position.y)
        screen.blit(self.pic, (self.position_int-self.size/2) )
            