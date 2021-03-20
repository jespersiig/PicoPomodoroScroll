import math
import utime
import picoscroll

picoscroll.init()

def pomocycle():

    # Set up our variables
    width = picoscroll.get_width()
    height = picoscroll.get_height()
    column = width-1
    row = height-1
    phase = "work"
    workminutes = 25
    restminutes = 5
    multiplier = math.trunc(10*workminutes*60/width/height)

    # Start counting down
    while not(picoscroll.is_pressed(picoscroll.BUTTON_Y)):

        # Illuminate every LED on the board
        for x in range(width):
            for y in range(height):
                picoscroll.set_pixel(x, y, 64)
        picoscroll.update()   
        
        # Extinguish LEDs one by one
        while row > -1:
            while column > -1:
                for x in range(multiplier):
                    if not(picoscroll.is_pressed(picoscroll.BUTTON_Y)):
                           utime.sleep(0.1)
                    else:
                        break
                picoscroll.set_pixel(column, row, 0)
                picoscroll.update()
                column -= 1
            column = width-1
            row -= 1
        row = height-1
        
        # No more LEDs? Switch from work to rest and vice versa
        if phase == "work":
            phase = "rest"
            multiplier = math.trunc(10*restminutes*60/width/height)
        elif phase == "rest":
            phase = "work"
            multiplier = math.trunc(10*workminutes*60/width/height)
        pass

    # Clear the display
    picoscroll.clear()
    picoscroll.update()

while True:
    while picoscroll.is_pressed(picoscroll.BUTTON_X):
        pomocycle()
