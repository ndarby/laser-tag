'''
Created on Jul. 16, 2019

@author: Nate
'''

import arcade

class Player(arcade.Sprite):
    '''
    classdocs
    '''
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        
        
    

    def __init__(self, filename, scale):
        '''
        Constructor
        '''
        
        super().__init__(filename, scale)
        
        