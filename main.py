def on_button_pressed_a():
    for index in range(3):
        music.play_tone(262, music.beat(BeatFraction.QUARTER))
        basic.show_number(3 - index)
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    basic.show_string("Go!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.play(music.tone_playable(175, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_number(input.temperature())
input.on_button_pressed(Button.B, on_button_pressed_b)
