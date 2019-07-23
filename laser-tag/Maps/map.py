'''
Created on Jul. 12, 2019

@author: spencercomin
'''

import arcade

class Map:
    '''
    classdocs
    '''
    # class constants
    scaling = 1

    def __init__(self, filename, tilefile = None):
        '''
        Constructor
        '''
        self.rawMap = arcade.read_tiled_map(filename, self.scaling, tilefile)

    def getSpriteLists(self):
        spriteLists = {}
        for name, grid in self.rawMap.layers.items():
            layer = arcade.SpriteList()
            for row in grid:
                for location in row:
                    if location.tile is not None:
                        tileSprite = arcade.Sprite(location.tile.source, 1)
                        tileSprite.center_x = location.center_x
                        tileSprite.center_y = location.center_y
                        layer.append(tileSprite)
            spriteLists[name] = layer
        return spriteLists