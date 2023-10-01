from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
daco_character = load_image('Daco.png')
hand_character = load_image('hand_arrow.png')

def handle_events():
    global running
    global click_positions

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
            if event.button == SDL_BUTTON_LEFT:
                click_positions.append((x, y)) #좌클릭 누르면 추가
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def move_daco_to_next_position():
    global x1, y1, x2, y2, click_positions, right, left

    if len(click_positions) > 0:
        x2, y2 = click_positions[0]
        rightleft(x1, x2)

        # 다음 클릭으로 이동
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if distance <= 50:
            click_positions.pop(0)  # 가꺼워지면 삭제
        else:
            x1 += (x2 - x1) * 0.05
            y1 += (y2 - y1) * 0.05

def tuk_canvas():
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

def rightleft(x1, x2):
    global left, right

    if x2 > x1:
        right = True
        left = False
    else:
        left = True
        right = False

def draw():
    global x1, y1, frame

    clear_canvas()
    tuk_canvas()
    move_daco_to_next_position()

    # 클릭하면 hand 그린다
    for x, y in click_positions:
        hand_character.draw(x, y)

    if right:
        daco_character.clip_draw(frame * 121, 122, 121, 122, x1, y1, 120, 120)
    elif left:
        daco_character.clip_draw(frame * 121, 0, 121, 122, x1, y1, 120, 120)

    frame = (frame + 1) % 9
    delay(0.02)

    update_canvas()

running = True
tuk_canvas()
frame = 0
x1, y1 = TUK_WIDTH // 2, TUK_HEIGHT // 2
x2, y2 = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
right, left = False, False
click_positions = []

while running:
    handle_events()
    draw()

close_canvas()
