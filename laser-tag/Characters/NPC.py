'''
Created on Sep. 26, 2019

@author: spencercomin
'''
from Characters.Char import Character

class NPC(Character):
    '''
    classdocs
    '''
    def __init__(self, x, y, imgSrc):
        super().__init__(x, y, imgSrc)
        self.brain = npcAI()
        self.mode = self.brain.wander
        self.leader = None
    
    def update(self):
        self.mode()
        super().update()

class npcAI():
    def __init__(self):
        pass
    
    def wander(self):
        pass
    
    def follow(self):
        pass
    