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
    maxFollowDistance = 300
    minFollowDistance = 50
    turn = 80
    movementSpeed = 1
    shootCountMax = 50
    
    def __init__(self, x, y, imgSrc):
        super().__init__(x, y, imgSrc)
        self.obstructed = False
        self.isoDirection = self.N
        self.walkCount = 0
        self.moving = True
        self.birthplace = (x, y)
        self.shootCounter = self.shootCountMax
    
    def update(self):
        if self.target and self.minFollowDistance < spriteDistance(self, self.target) < self.maxFollowDistance:
            self.follow()
            self.shootHandler()
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
        x = self.center_x - self.target.center_x
        y = self.center_y - self.target.center_y
        if x < 0 and y < 0:
            self.isoDirection = self.E
        elif x < 0 and y > 0:
            self.isoDirection = self.S
        elif x > 0 and y < 0:
            self.isoDirection = self.N
        elif x > 0 and y > 0:
            self.isoDirection = self.W
        self.shootCounter -= 1
    
    def shootHandler(self):           
        if self.shootCounter <= 0:
            self.shoot()
            self.shootCounter = self.shootCountMax
    