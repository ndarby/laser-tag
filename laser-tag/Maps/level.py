'''
Created on Sep. 27, 2019

@author: spencercomin
'''
import arcade
from Characters.NPC import NPC

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
        self.characters = None
    
    def load(self, mapSpriteLists, levelNumber):
        self.floor = mapSpriteLists.get(f'Floor{levelNumber}')
        self.upstairs = mapSpriteLists.get(f'Stairs{levelNumber}')
        self.downstairs = mapSpriteLists.get(f'Stairs{levelNumber - 1}')
        self.walls = mapSpriteLists.get(f'Walls{levelNumber}')
        self.noWalk = mapSpriteLists.get(f'NoWalk{levelNumber}')
        self.furniture = mapSpriteLists.get(f'Furniture{levelNumber}')
        self.characters = arcade.SpriteList()
        startUpBlock = mapSpriteLists.get(f'StartUp{levelNumber}')
        startDownBlock = mapSpriteLists.get(f'StartDown{levelNumber}')
        NPCstarts = mapSpriteLists.get(f'NPCStart{levelNumber}')
        if startUpBlock:
            self.startUpX = startUpBlock.sprite_list[0].center_x
            self.startUpY = startUpBlock.sprite_list[0].center_y
        if startDownBlock:
            self.startDownX = startDownBlock.sprite_list[0].center_x
            self.startDownY = startDownBlock.sprite_list[0].center_y
        if NPCstarts:
            for startSpot in NPCstarts:
                self.characters.append(NPC(startSpot.center_x, startSpot.center_y, 'npc_imgs'))
                
    def draw(self):
        if self.downstairs:
            self.downstairs.draw()
        self.floor.draw()
        self.walls.draw()
        if self.upstairs:
            self.upstairs.draw()
        if self.furniture:
            self.furniture.draw()
    
    def update(self):
        pass
