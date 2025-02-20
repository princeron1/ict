def on_forever():
    music.play(music.string_playable("C D E F G A B C5 ", 120),
        music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)

led.plot(75)