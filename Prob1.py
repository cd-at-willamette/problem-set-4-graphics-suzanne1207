############################################################
# Name: Suzanne Gunderson
# Name(s) of anyone worked with: N/A
# Est time spent (hr): 1
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600

def draw_image():
    """ Creates a window and draws a student's creation"""

    # Creating the window
    gw = GWindow(WIDTH, HEIGHT)
    
    # And now it is your turn! Add your code below! Make sure you meet all the requirements!
    #background
    def my_rect(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)
    b = GRect(WIDTH, HEIGHT)
    b.set_filled(True)
    b.set_fill_color("black")
    gw.add(b)
    #moon
    m = GOval(150, 100, 300, 300)
    m.set_filled(True)
    m.set_fill_color("yellow")
    gw.add(m)
    #skyscrapers
    my_rect(0,200,100,400,"grey")
    my_rect(105,300,150,300,"grey")
    my_rect(260,250,125,350,"grey")
    my_rect(390,350,115,250,"grey")
    my_rect(510,215,100,415,"grey")
    #words
    gw.add(GLabel("Cityscape", WIDTH//2, HEIGHT//3))
    #line
    gw.add(GLine(50,0,50,WIDTH))
    gw.add(GLine(25,0,25,HEIGHT))
    gw.add(GLine(75,0,75,HEIGHT))




if __name__ == '__main__':
    draw_image()
