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
    scaling = 0.07

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        
        
    

    def __init__(self, x, y):
        '''
        Constructor
        '''
        
        super().__init__('Characters/char.jpg', self.scaling)
        self.center_x = x
        self.center_y = y        