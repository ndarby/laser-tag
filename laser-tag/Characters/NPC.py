'''
Created on Sep. 26, 2019

@author: spencercomin
'''
from Characters.Char import Character

def spriteDistance(spriteA, spriteB):
    return ((spriteA.center_x - spriteB.center_x)**2 + (spriteA.center_y - spriteB.center_y)**2)**0.5

class NPC(Character):
    '''
    classdocs
    '''
    followDistance = 20
    
    def __init__(self, x, y, imgSrc):
        super().__init__(x, y, imgSrc)
        self.leader = None
        self.obstructed = False
    
    def update(self):
        if self.leader and spriteDistance(self, self.leader) > self.followDistance:
            self.follow()
        else:
            self.wander()

        super().update()
    
    def wander(self):
        pass
    
    def follow(self):
        pass
    