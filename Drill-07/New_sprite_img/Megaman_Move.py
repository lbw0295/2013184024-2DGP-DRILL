from pico2d import *

open_canvas()

Mega = load_image('Megaman.png')

frame = 0
cleft = 0
cright = 0
wid = 0
hei = 0

def teleport():
    x = 0
    y = 0
    cleft = 2
    wid = 0
    cright = 1904
    hei = 48
    for x in range(0, 13):
        cleft = cleft + wid + 2
        if x == 0:
            wid = 4
        elif x == 1:
            wid = 8
        elif x == 2:
            wid = 10
        elif x == 3:
            wid = 16
        elif x == 4:
            wid = 32
        elif x == 5:
            wid = 40
        elif 5  < x < 10 :
            wid = 38
        elif x == 10:
            wid = 34
        else:
            wid = 37


        clear_canvas()
        Mega.clip_draw(cleft, cright, wid, hei, 100, 100)
        update_canvas()
        x = x + 1
        get_events()
        delay(0.1)

def Standing():
    x = 0
    cleft = 2
    cright = 1848
    wid = 0
    hei = 44

    for x in range(0,8):
        cleft = cleft + wid + 2
        if x < 4:
            wid = 37
        else:
            wid = 33

        clear_canvas()
        Mega.clip_draw(cleft, cright, wid, hei, 100, 100)
        update_canvas()
        x = x + 1
        get_events()
        delay(0.1)

def Moving():
    x = 0
    y1 = 0
    y2 = 0
    cleft = 2
    cright = 1795
    wid = 0
    hei = 43

    for x in range(0, 12):
        cleft = cleft + wid + 2
        if x == 0:
            wid = 36
        elif x == 1:
            wid = 30
        elif x == 2:
            wid = 27
        elif x == 3:
            wid = 33
        elif x == 4:
            wid = 40
        elif x == 5:
            wid = 37
        elif x == 6:
            wid = 29
        elif x == 7:
            wid = 25
        elif x == 8:
            wid = 37
        elif x == 9:
            wid = 42
        elif x == 10:
            wid = 38
        elif x == 11:
            wid = 29

        clear_canvas()
        Mega.clip_draw(cleft, cright, wid, hei, 100, 100)
        update_canvas()
        x = x + 1
        get_events()
        delay(0.1)



while(True):
    teleport()
    Standing()
    Moving()