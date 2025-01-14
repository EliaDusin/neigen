def on_gesture_tilt_right():
    Spieler.change(LedSpriteProperty.X, 1)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_up():
    Spieler.change(LedSpriteProperty.Y, 1)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_tilt_left():
    Spieler.change(LedSpriteProperty.X, -1)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_logo_down():
    Spieler.change(LedSpriteProperty.Y, -1)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

Apfel: game.LedSprite = None
Spieler: game.LedSprite = None
Punkte = 0
Spieler = game.create_sprite(2, 2)
Zeit = 0

def on_forever():
    global Apfel, Punkte
    if Apfel.get(LedSpriteProperty.X) == Spieler.get(LedSpriteProperty.X):
        if Apfel.get(LedSpriteProperty.Y) == Spieler.get(LedSpriteProperty.Y):
            Apfel = game.create_sprite(randint(0, 5), randint(0, 5))
            Punkte += 1
basic.forever(on_forever)

def on_forever2():
    global Zeit
    basic.pause(1000)
    Zeit += 1
    if Zeit == 60:
        basic.show_string("Time´s up! Score:")
        basic.show_number(Punkte)
        game.game_over()
basic.forever(on_forever2)
