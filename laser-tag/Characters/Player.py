'''
Created on Sep. 26, 2019

@author: spencercomin
'''
from Characters.Char import Character

class Player(Character):
    '''
    classdocs
    '''
    pass

    def __init__(self, x, y, imgSrc):
        super().__init__(x, y, imgSrc)
        self.score = 0;