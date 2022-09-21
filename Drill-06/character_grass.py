from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90

while(True):
    if x < 800 and y <= 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x , y)
        x = x + 2
        delay(0.01)
        
    elif x >= 800 and y < 500:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x , y)
        y = y + 2
        delay(0.01)

    elif y >= 500 and x > 0:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x , y)
        x = x - 2
        delay(0.01)

    else :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x , y)
        y = y - 2
        delay(0.01)
    

close_canvas()
