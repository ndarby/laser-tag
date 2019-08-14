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

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        
        if self.change_x > 0 and self.change_y > 0:
            self.set_texture(1)
        elif self.change_x > 0 and self.change_y < 0:
            self.set_texture(0)
        elif self.change_x < 0 and self.change_y < 0:
            self.set_texture(2)
        elif self.change_x < 0 and self.change_y > 0:
            self.set_texture(3)
        elif self.change_x > 0 and self.change_y == 0:
            self.set_texture(4)
        elif self.change_x == 0 and self.change_y > 0:
            self.set_texture(5)
        elif self.change_x == 0 and self.change_y < 0:
            self.set_texture(6)
        elif self.change_x < 0 and self.change_y == 0:
            self.set_texture(7)
        
    

    def __init__(self, x, y):
        '''
        Constructor
        '''
        super().__init__()
        
        texture = arcade.load_texture("Characters/sprite-E.png", scale = self.scaling)
        self.textures.append(texture)
        texture = arcade.load_texture("Characters/sprite-N.png", scale = self.scaling)
        self.textures.append(texture)
        texture = arcade.load_texture("Characters/sprite-S.png", scale = self.scaling)
        self.textures.append(texture)
        texture = arcade.load_texture("Characters/sprite-W.png", scale = self.scaling)
        self.textures.append(texture)
        texture = arcade.load_texture("Characters/sprite-NE.png", scale = self.scaling)
        self.textures.append(texture)
        texture = arcade.load_texture("Characters/sprite-NW.png", scale = self.scaling)
        self.textures.append(texture)
        texture = arcade.load_texture("Characters/sprite-SE.png", scale = self.scaling)
        self.textures.append(texture)
        texture = arcade.load_texture("Characters/sprite-SW.png", scale = self.scaling)
        self.textures.append(texture)
        
        self.set_texture(0)
        self.center_x = x
        self.center_y = y  
            
        