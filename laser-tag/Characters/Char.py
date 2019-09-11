'''
Created on Jul. 16, 2019

@author: Nate
'''

import arcade

class Player(arcade.Sprite):
    '''
    classdocs
    '''
    #constants
    scaling = 0.4
    movementSpeed = 4
    N, NE, E, SE, S, SW, W, NW = 0, 1, 2, 3, 4, 5, 6, 7
    isoXScale = 2 / 5**0.5
    isoYScale = 1 / 5**0.5

    def update(self):
        self.change_x, self.change_y = 0, 0
        
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
        
            self.set_texture(self.isoDirection)
            
        
    

    def __init__(self, x, y):
        '''
        Constructor
        '''
        super().__init__()
        
        texture = arcade.load_texture("Characters/sprite-N.png", scale = self.scaling)
        self.textures.append(texture)
        texture = arcade.load_texture("Characters/sprite-NE.png", scale = self.scaling)
        self.textures.append(texture)
        texture = arcade.load_texture("Characters/sprite-E.png", scale = self.scaling)
        self.textures.append(texture)
        texture = arcade.load_texture("Characters/sprite-SE.png", scale = self.scaling)
        self.textures.append(texture)
        texture = arcade.load_texture("Characters/sprite-S.png", scale = self.scaling)
        self.textures.append(texture)
        texture = arcade.load_texture("Characters/sprite-SW.png", scale = self.scaling)
        self.textures.append(texture)
        texture = arcade.load_texture("Characters/sprite-W.png", scale = self.scaling)
        self.textures.append(texture)
        texture = arcade.load_texture("Characters/sprite-NW.png", scale = self.scaling)
        self.textures.append(texture)
        
        self.set_texture(0)
        self.center_x = x
        self.center_y = y
        self.isoDirection = None
            
        