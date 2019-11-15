'''
Created on Nov. 9, 2019

@author: spencercomin
'''

import arcade

class StatsScreen(object):
    '''
    classdocs
    '''


    def __init__(self, game):
        '''
        Constructor
        '''
        self.game = game
    
#     def update(self):
#         print(self.game.score)
    
    def draw(self):
        arcade.draw_text(f'Score: {self.game.score}', self.game.viewLeft + 15, self.game.viewBottom + 15, arcade.color.WHITE, font_size=36)
        print("stats drawing")