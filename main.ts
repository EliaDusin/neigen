input.onGesture(Gesture.TiltRight, function () {
    Spieler.change(LedSpriteProperty.X, 1)
})
input.onGesture(Gesture.LogoUp, function () {
    Spieler.change(LedSpriteProperty.Y, 1)
})
input.onGesture(Gesture.TiltLeft, function () {
    Spieler.change(LedSpriteProperty.X, -1)
})
input.onGesture(Gesture.LogoDown, function () {
    Spieler.change(LedSpriteProperty.Y, -1)
})
let Spieler: game.LedSprite = null
let Punkte = 0
Spieler = game.createSprite(2, 2)
let Zeit = 0
let Apfel = game.createSprite(randint(0, 5), randint(0, 5))
basic.forever(function () {
    if (Apfel.get(LedSpriteProperty.X) == Spieler.get(LedSpriteProperty.X)) {
        if (Apfel.get(LedSpriteProperty.Y) == Spieler.get(LedSpriteProperty.Y)) {
            Apfel.set(LedSpriteProperty.X, randint(0, 5))
            Apfel.set(LedSpriteProperty.Y, randint(0, 5))
            Punkte += 1
        }
    }
})
basic.forever(function () {
    basic.pause(1000)
    Zeit += 1
    if (Zeit == 60) {
        basic.showString("Time´s up! Score:")
        basic.showNumber(Punkte)
        game.gameOver()
    }
})
