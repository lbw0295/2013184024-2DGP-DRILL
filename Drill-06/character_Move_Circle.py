from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

de = 0
x = 400
y = 300
r = 200

while(True):
    if de <= 360 :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now((x + r * math.cos(math.radians(de))), (y + r * math.sin(math.radians(de))))
        de = de + 1
        delay(0.01)
    else :
        de = 0
