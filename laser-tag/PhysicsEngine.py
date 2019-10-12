'''
Created on Oct. 11, 2019

@author: spencercomin
'''

from arcade.geometry import check_for_collision_with_list
from arcade.sprite import Sprite
from arcade.sprite_list import SpriteList

class PhysicsEngine:
    '''
    an edit of the arcade PhysicsEngineSimple to include multiple characters
    this code is essentially a copy and paste from arcade.physics_engines.py
    '''

    def __init__(self, characters: SpriteList, walls: SpriteList):
        """
        Constructor.
        """
        assert(isinstance(characters, SpriteList))
        assert(isinstance(walls, SpriteList))
        self.characters = characters
        self.walls = walls

    def update(self):
        """
        Move everything and resolve collisions.
        """
        # --- Move in the x direction
        for char in self.characters:    
            char.center_x += char.change_x

            # Check for wall hit
            hit_list = \
            check_for_collision_with_list(char, self.walls)

            # If we hit a wall, move so the edges are at the same point
            if len(hit_list) > 0:
                if char.change_x > 0:
                    for item in hit_list:
                        char.right = min(item.left, char.right)
                elif char.change_x < 0:
                    for item in hit_list:
                        char.left = max(item.right, char.left)
                else:
                    raise RuntimeError(f"Error, collision while {char} wasn't moving.")
    
            # --- Move in the y direction
            char.center_y += char.change_y
    
            # Check for wall hit
            hit_list = \
                check_for_collision_with_list(char, self.walls)
    
            # If we hit a wall, move so the edges are at the same point
            if len(hit_list) > 0:
                if char.change_y > 0:
                    for item in hit_list:
                        char.top = min(item.bottom, char.top)
                elif char.change_y < 0:
                    for item in hit_list:
                        char.bottom = max(item.top, char.bottom)
                else:
                    raise RuntimeError(f"Error, collision while {char} wasn't moving.")

