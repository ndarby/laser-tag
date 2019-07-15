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
    mapScaling = 1
    tileScaling = 1

    def __init__(self, filename):
        '''
        Constructor
        '''
        self.rawMap = arcade.read_tiled_map(filename, self.scaling)
        px, py = arcade.isometric_grid_to_screen(self.rawMap.width // 2, self.rawMap.height //2, self.rawMap.width, self.rawMap.height, self.rawMap.tilewidth, self.rawMap.tileheight)

    def getSpriteLists(self):
        spriteLists = {}
        for name, grid in self.rawMap.items():
            layer = arcade.SpriteList()
            for row in grid:
                for gridLocation in row:
                    if gridLocation:
                        cell = arcade.Sprite(gridLocation.tile.source, self.tileScaling)
                        cell.center_x = gridLocation.center_x * self.tileScaling
                        cell.center_y = gridLocation.center_y * self.tileScaling
                        layer.append(cell)
            spriteLists[name] = layer
        return spriteLists