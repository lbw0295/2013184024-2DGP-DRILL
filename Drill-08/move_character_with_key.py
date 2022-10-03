from pico2d import *


def handle_events():
    global running
    global dirx
    global diry
    global DirLR

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                DirLR = 100
                dirx += 1
            elif event.key == SDLK_LEFT:
                DirLR = 0
                dirx -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                DirLR = 300
                dirx -= 1
            elif event.key == SDLK_LEFT:
                DirLR = 200
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1

    pass


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
DirLR = 300
x = 800 // 2
y = 180 // 2
frame = 0
dirx = 0
diry = 0


while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, DirLR * 1, 100, 100, x, y)

    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    x += dirx * 5
    y += diry * 5

    delay(0.01)

close_canvas()

