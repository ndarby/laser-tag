'''
Created on Nov. 9, 2019

@author: spencercomin
'''

import arcade
import time
import datetime

class StatsScreen(object):
    '''
    classdocs
    '''


    def __init__(self, game):
        '''
        Constructor
        '''
        self.game = game
        self.startTime = time.time()
 
    def draw(self):
        timePassed = int(time.time()-self.startTime)
        arcade.draw_text(f'Score: {self.game.score}', self.game.viewLeft + 15, self.game.viewBottom + 60, arcade.color.WHITE, font_size=36)
        arcade.draw_text(f'Time: {datetime.timedelta(seconds=timePassed)}', self.game.viewLeft + 15, self.game.viewBottom + 15, arcade.color.WHITE, font_size=36)
