'''
Created on Jul. 16, 2019

@author: spencercomin
'''

import arcade
from Maps.map import Map
from Characters.Player import Player
from Maps.level import Level

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
    keyToDir = {
                0:None, 1:W, 2:E, 3:None,
                4:S, 5:SW, 6:SE, 7:S, 8:N,
                9:NW, 10:NE, 11:N, 12:None,
                13:W, 14:E, 15:None
                }


    def __init__(self, width = 1440, height = 900, title = 'Game', fullScreen = True):
        '''
        Constructor
        '''
        super().__init__(width, height, title, fullscreen=fullScreen)
        self.mapList = None
        #change later
        self.mapList = [Map('map1.tmx')]
        self.playerSprite = None
        
        self.currentMap = None
        self.currentLevel = 0
        self.levels = []
        self.characterList = None
        self.enemyList = None
        
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
        self.playerSprite = Player(startX, startY, 'player_imgs')
        self.characterList = self.levels[0].characters
        self.characterList.append(self.playerSprite)
        self.physicsEngine = arcade.PhysicsEngineSimple(self.playerSprite, self.levels[self.currentLevel].noWalk)
        
    
    def on_draw(self):
        arcade.start_render()
        self.levels[self.currentLevel].draw()
        self.characterList.draw()
    
    def _changeLevel(self, dLevel):
        assert dLevel in (1, -1)
        #remove the player form the current level's list of characters before changing level
        self.levels[self.currentLevel].characters.remove(self.playerSprite)
        self.currentLevel += dLevel
        self.physicsEngine.walls = self.levels[self.currentLevel].noWalk
        if dLevel == -1:
            self.playerSprite.center_x = self.levels[self.currentLevel].startDownX
            self.playerSprite.center_y = self.levels[self.currentLevel].startDownY
        else:
            self.playerSprite.center_x = self.levels[self.currentLevel].startUpX
            self.playerSprite.center_y = self.levels[self.currentLevel].startUpY
        self.characterList = self.levels[self.currentLevel].characters
        self.characterList.append(self.playerSprite)
        
    def _scrollUpdate(self):
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
                
    def update(self, delta_time):
        self.playerSprite.isoDirection = self.keyToDir[self.directionKey]
        if self.directionKey == 0:
            self.playerSprite.moving = False
        else:
            self.playerSprite.moving = True
        
        self.characterList.update()
        self.physicsEngine.update()
              
        # Check stairs
        if self.levels[self.currentLevel].upstairs:
            if arcade.check_for_collision_with_list(self.playerSprite, self.levels[self.currentLevel].upstairs):
                self._changeLevel(1)
        if self.levels[self.currentLevel].downstairs:
            if arcade.check_for_collision_with_list(self.playerSprite, self.levels[self.currentLevel].downstairs):
                self._changeLevel(-1)
        
        self._scrollUpdate()
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.close()
            
        if key == arcade.key.UP:
            self.directionKey += 8
        if key == arcade.key.DOWN:
            self.directionKey += 4
        if key == arcade.key.RIGHT:
            self.directionKey += 2
        if key == arcade.key.LEFT:
            self.directionKey += 1
    
    def on_key_release(self, key, modifiers):
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
