'''
Created on Jul. 16, 2019

@author: spencercomin
'''

import arcade
from game import Game

if __name__ == '__main__':
    window = Game()
    window.setup()
    arcade.run()