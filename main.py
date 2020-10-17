"""
Chess Clone

"""

import arcade
# Screen title and size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Chess"
SQUARE_SIZE = 600/8

"""
TODO
* Drag and Drop
* Snap to place
* Dots to show possible moves
"""

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        self.black_set = None
        self.white_set = None

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False)
        arcade.set_background_color(arcade.color.AMAZON)
    
    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # All black pawns share a Y coordinate
        self.black_set = arcade.SpriteList()        
        x= SQUARE_SIZE/2 
        y = SQUARE_SIZE/2 + SQUARE_SIZE
        for _ in range (8):
            temp = arcade.Sprite("Chess_Pieces\pawn_black.png")
            temp.position = (x,y) # X,Y
            self.black_set.append(temp)    
            x= x + SQUARE_SIZE 
        self.white_set = arcade.SpriteList()
        
        # Positioning white pawns
        x= SQUARE_SIZE/2 
        y = SQUARE_SIZE/2 + 6 * SQUARE_SIZE
        for _ in range (8):
            temp = arcade.Sprite("Chess_Pieces\pawn_white.png")
            temp.position = (x,y) # X,Y
            self.white_set.append(temp)    
            x= x + SQUARE_SIZE 
            
        # All black other pieces share a Y coordinate (Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)
        piece = ["rook","horse","bishop","queen","king","bishop","horse","rook"]
        x= SQUARE_SIZE/2
        y= SQUARE_SIZE/2  
        for i in range (8):
            temp = arcade.Sprite(f"Chess_Pieces\{piece[i]}_black.png")
            temp.position = (x,y) # X,Y
            self.black_set.append(temp)    
            x= x + SQUARE_SIZE 
        
        
        x= SQUARE_SIZE/2
        y= SQUARE_SIZE/2 + 7 * SQUARE_SIZE  
        for i in range (8):
            temp = arcade.Sprite(f"Chess_Pieces\{piece[i]}_white.png")
            temp.position = (x,y) # X,Y
            self.white_set.append(temp)    
            x= x + SQUARE_SIZE     
            
    def on_draw(self):
        arcade.start_render()
        square_size = SCREEN_HEIGHT/8
        x,y =square_size/2 , square_size/2
        colors = [arcade.color.AMAZON,arcade.color.WHITE]

        for _ in range(8):
            for i in range(8):
                if i % 2 ==0:
                    arcade.draw_rectangle_filled(x,y, square_size, square_size ,colors[0])
                else:
                    arcade.draw_rectangle_filled(x,y, square_size, square_size ,colors[1])
                x += square_size
            y += square_size
            x = square_size / 2
            colors.reverse()
        self.black_set.draw()
        self.white_set.draw()
        
    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
    

        pass
    

    def on_mouse_release(self, x: float, y: float, button: int,  modifiers: int):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """
        pass


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()











