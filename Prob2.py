########################################
# Name: Suzanne Gunderson
# Collaborators: N/A
# Estimated time spent (hrs): 3
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """

    gw = GWindow(WIDTH, HEIGHT)

    # You got it from here
    draw_rows()

def draw_rows():
    gw = GWindow(WIDTH,HEIGHT)
    for i in range(BRICKS_IN_BASE): # loops for each row
        BRICKS_IN_ROW = BRICKS_IN_BASE - i # each row has one less brick each time
        X = (WIDTH - BRICKS_IN_ROW * BRICK_WIDTH) //2 # x is the length of the row divided by 2 so it's centered
        Y = (HEIGHT - (BRICKS_IN_BASE * BRICK_HEIGHT)) //2 + (BRICK_HEIGHT * BRICKS_IN_BASE) - (BRICK_HEIGHT * (i+1)) # y takes the height of the entire pyramid from the height and divides it in two to center it, then adds the rows yet to be added
        for i in range(BRICKS_IN_ROW):
            b = GRect(X, Y, BRICK_WIDTH, BRICK_HEIGHT) # draws a brick
            gw.add(b) # adds the brick
            X = X + BRICK_WIDTH # x changes for each brick in the row
            Y = Y # y stays the same for each brick in the row



if __name__ == '__main__':
    draw_pyramid()
