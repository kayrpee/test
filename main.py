def on_button_pressed_a():
    music.play_melody("E B C5 A B G A F ", 120)
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_number(6)
basic.pause(10000)
basic.clear_screen()

def on_forever():
    pass
basic.forever(on_forever)
