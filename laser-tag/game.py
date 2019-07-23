'''
Created on Jul. 16, 2019

@author: spencercomin
'''

import arcade
from Maps.map import Map

class Game(arcade.Window):
    '''
    classdocs
    '''
    #constant
    mapcount = 1
    background = arcade.color.BLACK
    viewportMargin = 300


    def __init__(self, width = 1440, height = 900, title = 'Game', fullScreen = True):
        '''
        Constructor
        '''
        super().__init__(width, height, title, fullscreen=fullScreen)
        self.mapList = None
        #change later
        self.mapList = [Map('map1.tmx')]   
        #
        self.currentMap = None
        self.wallList = None
        self.floorList = None
        
        self.leftPressed = False
        self.rightPressed = False
        self.upPressed = False
        self.downPressed = False
        
        arcade.set_background_color(self.background)
        
        
    def setup(self):
        
        
        self.currentMap = self.mapList[0].getSpriteLists()        
        self.wallList = self.currentMap['Walls']
        self.floorList = self.currentMap['Floor']
        
    
    def on_draw(self):
        arcade.start_render()
        self.floorList.draw()
        self.wallList.draw()
    
    def update(self, delta_time):
        self.floorList.update()
        self.wallList.update()
    
    def on_key_press(self, key, modifiers:int):
        if key == arcade.key.ESCAPE or key == arcade.key.Q and modifiers in (arcade.key.LCOMMAND, arcade.key.RCOMMAND):
            self.close()
            
        if key == arcade.key.UP:
            pass
        if key == arcade.key.DOWN:
            pass
        if key == arcade.key.LEFT:
            pass
        if key == arcade.key.RIGHT:
            pass
    
    def on_key_release(self, symbol:int, modifiers:int):
        pass
    
    def on_mouse_motion(self, x:float, y:float, dx:float, dy:float):
        pass