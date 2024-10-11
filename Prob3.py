########################################
# Name: Suzanne Gunderson
# Collaborators: N/A
# Estimate time spent (hrs): 3
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score

def clicky_box():
    # Defining the callback function, which you won't need until Part C
    def on_mouse_down(event):
        if event.get_x() >= sq.get_x() and event.get_x() <= (sq.get_x() + SQUARE_SIZE):
            if event.get_y() >= sq.get_y() and event.get_y() <= (sq.get_y() + SQUARE_SIZE):
                new_x_coordinate = random.randint(0,GW_WIDTH)
                new_y_coordinate = random.randint(0,GW_HEIGHT)
                sq.set_location(new_x_coordinate,new_y_coordinate)
                x_coordinate = new_x_coordinate
                y_coordinate = new_y_coordinate
                gw.remove(score)
                gw.score += 1
                score.set_label(f"{gw.score}")
                gw.add(score)
        else:
            gw.remove(score)
            gw.score = 0
            score.set_label(f"{gw.score}")
            gw.add(score)


    # Down here you should initialize the window and draw the initial square
    # Make sure you tab it in so that it is part of the clicky_box function
    
    gw = GWindow(GW_WIDTH, GW_HEIGHT)
    
    # Draw Initial Square:
    X = (GW_HEIGHT-SQUARE_SIZE)//2
    Y = (GW_HEIGHT-SQUARE_SIZE)//2
    sq = GRect(X,Y,SQUARE_SIZE,SQUARE_SIZE)
    sq.set_color("purple")
    sq.set_filled(True)
    gw.add(sq)
    x_coordinate = sq.get_x()
    y_coordinate = sq.get_y()
    print(x_coordinate, y_coordinate)
    gw.score = 0
    score = GLabel(f"{gw.score}",SCORE_DX,SCORE_DY)
    gw.add(score)
    #gw.add(GLabel(Score,SCORE_DX,SCORE_DY))
    gw.add_event_listener("click", on_mouse_down)




if __name__ == '__main__':
    clicky_box()
