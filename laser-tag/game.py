'''
Created on Jul. 16, 2019

@author: spencercomin
'''

import arcade
from Maps.map import Map
from Characters.Char import Player

class Game(arcade.Window):
    '''
    classdocs
    '''
    #constants
    mapcount = 1
    background = arcade.color.BLACK
    viewportMargin = 300
    movementSpeed = 3


    def __init__(self, width = 1440, height = 900, title = 'Game', fullScreen = True):
        '''
        Constructor
        '''
        super().__init__(width, height, title, fullscreen=fullScreen)
        self.mapList = None
        #change later
        self.mapList = [Map('map1.tmx')]   
        #
        self.playerSprite = None
        
        self.currentMap = None
        self.wallList = None
        self.floorList = None
        self.playerList = None
        
        self.leftPressed = False
        self.rightPressed = False
        self.upPressed = False
        self.downPressed = False
        
        arcade.set_background_color(self.background)
        
        
    def setup(self):
        
        self.currentMap = self.mapList[0].getSpriteLists()        
        self.wallList = self.currentMap['Walls']
        self.floorList = self.currentMap['Floor']
        self.playerSprite = Player(700, 400)
        self.playerList = arcade.SpriteList()
        self.playerList.append(self.playerSprite)
        
    
    def on_draw(self):
        arcade.start_render()
        self.floorList.draw()
        self.playerList.draw()
        self.wallList.draw()
    
    def update(self, delta_time):
        self.floorList.update()
        self.wallList.update()
    
        self.playerSprite.change_x, self.playerSprite.change_y = 0, 0
        
        if self.upPressed and not self.downPressed:
            self.playerSprite.change_y = self.movementSpeed
        elif self.downPressed and not self.upPressed:
            self.playerSprite.change_y = -self.movementSpeed
        if self.leftPressed and not self.rightPressed:
            self.playerSprite.change_x = -self.movementSpeed
        elif self.rightPressed and not self.leftPressed:
            self.playerSprite.change_x = self.movementSpeed
            
        self.playerList.update()
    
    def on_key_press(self, key, modifiers:int):
        if key == arcade.key.ESCAPE or key == arcade.key.Q and modifiers in (arcade.key.LCOMMAND, arcade.key.RCOMMAND):
            self.close()
            
        if key == arcade.key.UP:
            self.upPressed = True
        if key == arcade.key.DOWN:
            self.downPressed = True
        if key == arcade.key.LEFT:
            self.leftPressed = True
        if key == arcade.key.RIGHT:
            self.rightPressed = True
    
    def on_key_release(self, key, modifiers:int):
        if key == arcade.key.UP:
            self.upPressed = False
        elif key == arcade.key.DOWN:
            self.downPressed = False
        elif key == arcade.key.LEFT:
            self.leftPressed = False
        elif key == arcade.key.RIGHT:
            self.rightPressed = False
    
    def on_mouse_motion(self, x:float, y:float, dx:float, dy:float):
        pass