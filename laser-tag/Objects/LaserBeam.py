'''
Created on Oct. 1, 2019

@author: spencercomin
'''
import arcade

class LaserBeam():
    '''
    classdocs
    '''
    speed = 10
    length = 20
    width = 3

    def __init__(self, x, y, targetX, targetY, color=arcade.color.RED):
        '''
        Constructor
        '''
        super().__init__()
        self.center_x = x
        self.center_y = y
        distance = ((x-targetX)**2 + (y-targetY)**2)**0.5
        self.change_x = (targetX - x)*self.speed/distance
        self.change_y = (targetY - y)*self.speed/distance
        self.color = color
    
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
    
    def draw(self):
        ratio = self.length/self.speed
        arcade.draw_line(self.center_x, self.center_y, self.center_x + self.change_x*ratio,
                         self.center_y + self.change_y*ratio, self.color, line_width=self.width)