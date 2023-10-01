from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
daco_character = load_image('Daco.png')
hand_character = load_image('hand_arrow.png')

def handle_events():
    global running
    global x2, y2
    global click_positions

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x2, y2 = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x2, y2 = event.x, TUK_HEIGHT - 1 - event.y
            if event.button == SDL_BUTTON_LEFT:
                click_positions.append((x2, y2))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

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

def draw_line():
    global x1, y1, x2, y2

    x1 = (1 - 0.05) * x1 + 0.05 * x2
    y1 = (1 - 0.05) * y1 + 0.05 * y2

running = True
tuk_canvas()
frame = 0
x1, y1 = TUK_WIDTH // 2, TUK_HEIGHT // 2
x2, y2 = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)

right, left = False, False

click_positions = []  # 마우스 클릭한 위치를 저장할 리스트
current_position = None  # 현재 이동 중인 위치

while running:
    clear_canvas()
    tuk_canvas()
    rightleft(x1, x2)
    handle_events()
    pos_x, pos_y = x2, y2

    # 마우스 클릭한 위치에 hand_character 그리기
    for pos_x, pos_y in click_positions:
        hand_character.draw(pos_x, pos_y)


    if right:
        daco_character.clip_draw(frame * 121, 122, 121, 122, x1, y1, 120, 120)
    elif left:
        daco_character.clip_draw(frame * 121, 0, 121, 122, x1, y1, 120, 120)

    frame = (frame + 1) % 9
    delay(0.02)
    draw_line()

    if current_position:
        # 현재 이동 중인 위치와 daco_character가 겹치면 해당 위치를 제거합니다.
        distance = (current_position[0] - x1) ** 2 + (current_position[1] - y1) ** 2
        if distance <= 50:
            click_positions.remove(current_position)
            current_position = None

    if not current_position and click_positions:
        # 아직 이동 중인 위치가 없고 클릭 위치가 남아있다면,
        # 다음 클릭 위치를 가져와서 이동을 시작합니다.
        current_position = click_positions[0]
        click_positions = click_positions[1:]

    update_canvas()
