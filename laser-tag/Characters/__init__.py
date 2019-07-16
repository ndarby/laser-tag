import Characters.Char
import Characters.MyGame
import arcade

if __name__ == '__main__':
    window = Characters.MyGame.MyClass(600, 600, "test")
    window.setup()
    arcade.run()
    