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
    turn = 80
    movementSpeed = 1
    
    def __init__(self, x, y, imgSrc):
        super().__init__(x, y, imgSrc)
        self.leader = None
        self.obstructed = False
        self.isoDirection = self.N
        self.walkCount = 0
        self.moving = True
        
    
    def update(self):
        if self.leader and spriteDistance(self, self.leader) > self.followDistance:
            self.follow()
        else:
            self.wander()            

        super().update()
    
    def wander(self):
        self.walkCount += 1
        if self.walkCount > self.turn:
            self.walkCount = 0
            if self.isoDirection == self.N:
                self.isoDirection = self.E
            elif self.isoDirection == self.E:
                self.isoDirection = self.S
            elif self.isoDirection == self.S:
                self.isoDirection = self.W
            elif self.isoDirection == self.W:
                self.isoDirection = self.N                
                
    
    def follow(self):
        pass
    