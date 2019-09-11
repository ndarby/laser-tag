'''
Created on Jul. 16, 2019

@author: spencercomin
'''

import arcade
from Maps.map import Map
from Characters.Char import Player

class Level:
    
    def __init__(self):
        self.upstairs = None
        self.downstairs = None
        self.floor = None
        self.walls = None
        self.noWalk = None
        self.furniture = None
        self.startUpX = None
        self.startUpY = None
        self.startDownX = None
        self.startDownY = None
    
    def load(self, mapSpriteLists, levelNumber):
        self.floor = mapSpriteLists.get(f'Floor{levelNumber}')
        self.upstairs = mapSpriteLists.get(f'Stairs{levelNumber}')
        self.downstairs = mapSpriteLists.get(f'Stairs{levelNumber - 1}')
        self.walls = mapSpriteLists.get(f'Walls{levelNumber}')
        self.noWalk = mapSpriteLists.get(f'NoWalk{levelNumber}')
        self.furniture = mapSpriteLists.get(f'Furniture{levelNumber}')
        startUpBlock = mapSpriteLists.get(f'StartUp{levelNumber}')
        startDownBlock = mapSpriteLists.get(f'StartDown{levelNumber}')
        if startUpBlock:
            self.startUpX = startUpBlock.sprite_list[0].center_x
            self.startUpY = startUpBlock.sprite_list[0].center_y
        if startDownBlock:
            self.startDownX = startDownBlock.sprite_list[0].center_x
            self.startDownY = startDownBlock.sprite_list[0].center_y
        
    def draw(self):
        if self.downstairs:
            self.downstairs.draw()
        self.floor.draw()
        self.walls.draw()
        if self.upstairs:
            self.upstairs.draw()
        if self.furniture:
            self.furniture.draw()
        
    
    def postDraw(self):
        'currently not used, probably unnecessary'
        pass
        
    
    def update(self):
        pass

class Game(arcade.Window):
    '''
    classdocs
    '''
    #constants
    mapcount = 1
    background = arcade.color.BLACK
    viewportMargin = 300
    movementSpeed = 4
    levelCount = 3
    N, NE, E, SE, S, SW, W, NW = 0, 1, 2, 3, 4, 5, 6, 7
    keyToDir = {0:None, 1:6, 2:2, 3:None, 4:4, 5:5, 6:3, 7:4, 8:0, 9:7, 10:1, 11:0, 12:None, 13:6, 14:2, 15:None}


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
        self.currentLevel = 0
        self.levels = []
        self.playerList = None
        
        self.leftPressed = False
        self.rightPressed = False
        self.upPressed = False
        self.downPressed = False
        
        self.physicsEngine = None
        
        self.directionKey = 0
        
        self.viewLeft, self.viewBottom = 0, 0
        
        arcade.set_background_color(self.background)
        
        
    def setup(self):
        
        self.currentMap = self.mapList[0].getSpriteLists()
        
        for i in range(self.levelCount):
            levelAdd = Level()
            levelAdd.load(self.currentMap, i)
            self.levels.append(levelAdd)
        
        
        startX = self.currentMap['StartBlock'].sprite_list[0].center_x
        startY = self.currentMap['StartBlock'].sprite_list[0].center_y
        self.playerSprite = Player(startX, startY)
        self.playerList = arcade.SpriteList()
        self.playerList.append(self.playerSprite)
        self.physicsEngine = arcade.PhysicsEngineSimple(self.playerSprite, self.levels[self.currentLevel].noWalk)
        
    
    def on_draw(self):
        arcade.start_render()
        self.levels[self.currentLevel].draw()
        self.playerList.draw()
    
    def update(self, delta_time):        
        self.playerSprite.isoDirection = self.keyToDir[self.directionKey]
        
        self.playerList.update()
        self.physicsEngine.update()
        
        
        # Check stairs
        if self.levels[self.currentLevel].upstairs:
            if arcade.check_for_collision_with_list(self.playerSprite, self.levels[self.currentLevel].upstairs):
                self.currentLevel += 1
                self.physicsEngine.walls = self.levels[self.currentLevel].noWalk
                self.playerSprite.center_x = self.levels[self.currentLevel].startUpX
                self.playerSprite.center_y = self.levels[self.currentLevel].startUpY
        if self.levels[self.currentLevel].downstairs:
            if arcade.check_for_collision_with_list(self.playerSprite, self.levels[self.currentLevel].downstairs):
                self.currentLevel -= 1
                self.physicsEngine.walls = self.levels[self.currentLevel].noWalk
                self.playerSprite.center_x = self.levels[self.currentLevel].startDownX
                self.playerSprite.center_y = self.levels[self.currentLevel].startDownY
        
        changed = False

        # Scroll left
        left_bndry = self.viewLeft + self.viewportMargin
        if self.playerSprite.left < left_bndry:
            self.viewLeft -= left_bndry - self.playerSprite.left
            changed = True

        # Scroll right
        right_bndry = self.viewLeft + self.width - self.viewportMargin
        if self.playerSprite.right > right_bndry:
            self.viewLeft += self.playerSprite.right - right_bndry
            changed = True

        # Scroll up
        top_bndry = self.viewBottom + self.height - self.viewportMargin
        if self.playerSprite.top > top_bndry:
            self.viewBottom += self.playerSprite.top - top_bndry
            changed = True

        # Scroll down
        bottom_bndry = self.viewBottom + self.viewportMargin
        if self.playerSprite.bottom < bottom_bndry:
            self.viewBottom -= bottom_bndry - self.playerSprite.bottom
            changed = True

        if changed:
            arcade.set_viewport(self.viewLeft,
                                self.width + self.viewLeft,
                                self.viewBottom,
                                self.height + self.viewBottom)
    
    def on_key_press(self, key, modifiers:int):
        if key == arcade.key.ESCAPE or key == arcade.key.Q and modifiers in (arcade.key.LCOMMAND, arcade.key.RCOMMAND):
            self.close()
            
        if key == arcade.key.UP:
            self.directionKey += 8
        if key == arcade.key.DOWN:
            self.directionKey += 4
        if key == arcade.key.RIGHT:
            self.directionKey += 2
        if key == arcade.key.LEFT:
            self.directionKey += 1
    
    def on_key_release(self, key, modifiers:int):
        if key == arcade.key.UP:
            self.directionKey -= 8
        elif key == arcade.key.DOWN:
            self.directionKey -= 4
        elif key == arcade.key.RIGHT:
            self.directionKey -= 2
        elif key == arcade.key.LEFT:
            self.directionKey -= 1
    
    def on_mouse_motion(self, x:float, y:float, dx:float, dy:float):
        pass
