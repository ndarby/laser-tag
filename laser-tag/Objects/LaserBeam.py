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
    length = 5

    def __init__(self, x, y, targetX, targetY, color=arcade.color.WHITE):
        '''
        Constructor
        '''
        super().__init__()
        self.center_x = x
        self.center_y = y
        distance = ((x-targetX)**2 + (y-targetY)**2)**0.5
        self.change_x = (x - targetX)*self.speed/distance
        self.change_y = (y - targetY)*self.speed/distance
        self.color = color
    
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.draw()
    
    def draw(self):
        ratio = self.length/self.speed
        arcade.draw_line(self.center_x, self.center_y, self.center_x + self.change_x*ratio,
                         self.center_y + self.change_y*ratio, self.color, line_width=50)
        print('Draw')