'''
Created on Jul. 16, 2019

@author: Nate
'''

import arcade
import Characters.Char

class MyClass(arcade.Window):
    '''
    classdocs
    '''
    SPRITE_SCALING = 0.1
    MOVEMENT_SPEED = 3


    def __init__(self, width, height, title):
        '''
        Constructor
        '''
        super().__init__(width, height, title)
        
        self.player_list = None
        
        self.player_sprite = None
        
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
        
    def setup(self):
        
        self.player_list = arcade.SpriteList()
        self.player_sprite = Characters.Char.Player("char.jpg", self.SPRITE_SCALING)
        self.player_sprite.center_x = 300
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)
        
    def on_draw(self):
        
        arcade.start_render()
        self.player_list.draw()
        
    def update(self, delta_time):
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        
        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = self.MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -self.MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -self.MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = self.MOVEMENT_SPEED
            
        self.player_list.update()
        
    def on_key_press(self, key, modifiers):
        
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
            
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False   























        