from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
daco_character = load_image('Daco.png')
hand_character = load_image('hand_arrow.png')


def tuk_canvas():
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

def rightleft(x1,x2):
    global left,right

    if x2 > x1:
        right = True
        left = False
    else:
        left = True
        right = False


def draw_line():
    global x1, y1 , x2 ,y2

    #t = i / 100  # (0~1)까지
    x1 = (1 - 0.05) * x1 + 0.05 * x2
    y1 = (1 - 0.05) * y1 + 0.05 * y2

    distance = (x2 -x1)**2 +(y2-y1)**2
    if distance <= 50:
        x2,y2 =random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)


tuk_canvas()
frame = 0
x1 ,y1 = TUK_WIDTH // 2 , TUK_HEIGHT // 2
x2,y2 = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
right, left = False , False

while True:
    clear_canvas()
    tuk_canvas()
    rightleft(x1, x2)

    if right:
        daco_character.clip_draw(frame * 121, 122, 121, 122, x1, y1, 120, 120)
    elif left:
        daco_character.clip_draw(frame * 121, 0, 121, 122, x1, y1, 120, 120)

    hand_character.draw(x2,y2)

    frame = (frame + 1) % 9
    delay(0.02)
    draw_line()
    
    update_canvas()





