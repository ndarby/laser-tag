'''
Created on Jul. 16, 2019

@author: Nate
'''

import arcade
from Objects.LaserBeam import LaserBeam

class Character(arcade.Sprite):
    '''
    the base class for the player and NPCs
    '''
    #constants
    scaling = 1.3
    movementSpeed = 3.2
    stepSpeed = 16
    N, NE, E, SE, S, SW, W, NW = 0, 1, 2, 3, 4, 5, 6, 7
    isoXScale = 2 / 5**0.5
    isoYScale = 1 / 5**0.5

    def update(self):
        self.change_x, self.change_y = 0, 0
        for laser in self.lasers:
            laser.update()
        
        if self.isoDirection != None:
            if self.isoDirection == self.N:
                self.change_x = -self.isoXScale * self.movementSpeed
                self.change_y = self.isoYScale * self.movementSpeed
            elif self.isoDirection == self.NE:
                self.change_x = 0
                self.change_y = self.movementSpeed
            elif self.isoDirection == self.E:
                self.change_x = self.isoXScale * self.movementSpeed
                self.change_y = self.isoYScale * self.movementSpeed
            elif self.isoDirection == self.SE:
                self.change_x = self.movementSpeed
                self.change_y = 0
            elif self.isoDirection == self.S:
                self.change_x = self.isoXScale * self.movementSpeed
                self.change_y = -self.isoYScale * self.movementSpeed
            elif self.isoDirection == self.SW:
                self.change_x = 0
                self.change_y = -self.movementSpeed
            elif self.isoDirection == self.W:
                self.change_x = -self.isoXScale * self.movementSpeed
                self.change_y = -self.isoYScale * self.movementSpeed
            elif self.isoDirection == self.NW:
                self.change_x = -self.movementSpeed
                self.change_y = 0
        
            imgTypeIndex = 0
            if self.moving:
                self.movUpdateCount += 1
                imgTypeIndex = self.movUpdateCount%self.stepSpeed//(self.stepSpeed//2)
            else:
                self.movUpdateCount = 0
            if self.shootDirection:
                self.set_texture(3*self.shootDirection + imgTypeIndex)
            else:
                self.set_texture(3*self.isoDirection + imgTypeIndex)
            
        
    

    def __init__(self, x, y, imgSrc):
        '''
        Constructor
        '''
        super().__init__()
        
        for direction in ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']:
            for picture in ['stand', 'walk1', 'walk2']:
                texture = arcade.load_texture(f"Characters/{imgSrc}/sprite_{direction}_{picture}.png", scale=self.scaling)
                self.textures.append(texture)
                        
        self.set_texture(0)
        self.center_x = x
        self.center_y = y
        self.isoDirection = self.N
        self.moving = False
        self.movUpdateCount = 0
        self.shootDirection = None
        self.lasers = []
        self.target = None
    
    def shoot(self):
        self.lasers.append(LaserBeam(self.center_x, self.center_y, self.target.center_x, self.target.center_y))
        
        