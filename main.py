'''
Created on 11-Jun-2012

@author: NANDU
'''

from pygame import display, init, time, event, draw, key, font, mouse
from pygame.constants import *
from planets import PLANET
from initialise import screen
from gameobjects.vector2 import Vector2

class Game:
    def __init__(self):
        init()
        self.n = 3
        self.planets = {i:PLANET() for i in range(self.n)}
        self.cm_velocity_zero()
        display.set_caption('Planets')
        self.clock = time.Clock()
    
    def cm_velocity_zero(self):
        m = 0
        p = Vector2(0,0)
        for planet in self.planets.values():
            p = p + planet.velocity*planet.mass
            m = m + planet.mass
        p = p/float(m)
        for planet in self.planets.values():
            planet.velocity -= p 
        
    def update(self):
        for planet1 in self.planets.values():
            for key2, planet2 in self.planets.items():
                if planet1.position == planet2.position:
                    continue
                pos = planet2.position - planet1.position
                l = pos.length
                if l>planet2.size.x/4:
                    pos = pos/l**3
                    planet1.update_velocity(pos*planet2.mass)
                else:
                    if planet1.mass > planet2.mass:
                        planet1.velocity=(planet1.velocity*planet1.mass + planet2.mass*planet2.velocity)/(planet1.mass+planet2.mass)
                        planet1.mass += planet2.mass
                        del self.planets[key2]
        
        for planet in self.planets.values():
            planet.update_position()
            
    def draw(self):
        screen.fill((0,0,0))
        for planet in self.planets.values():
            planet.draw()
        display.update([[0,0],[screen.get_width(),screen.get_height()]])
        
    
    def reset(self):
        self.n = 0
        self.planets = {}
    
    def handle_events(self):
        keys = key.get_pressed()
        if keys[K_q] or keys[K_ESCAPE]:
            self.quit = True
       
        for evt in event.get():
            if evt.type == QUIT:
                self.quit = True
            if evt.type == MOUSEBUTTONUP:
                self.planets[self.n]=PLANET(Vector2(mouse.get_pos()))
                self.cm_velocity_zero()
                self.n += 1
            if evt.type == KEYDOWN:
                self.quit = True
        
    def run(self):
        self.quit = False
        self.stop = False
        while not self.quit:
            
            self.handle_events()
            
            if not self.stop:
                self.update()
                self.draw()
            #self.clock.tick(1000)

if __name__ == '__main__':
    game = Game()
    game.run()