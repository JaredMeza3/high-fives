IsLogging = False

def on_button_pressed_a():
    global IsLogging
    datalogger.delete_log()
    IsLogging = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global IsLogging
    IsLogging = False
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_every_interval():
    if IsLogging:
        basic.show_icon(IconNames.SMALL_DIAMOND)
        basic.clear_screen()
        datalogger.log(datalogger.create_cv("AX", input.acceleration(Dimension.X)),
            datalogger.create_cv("AY", input.acceleration(Dimension.Y)),
            datalogger.create_cv("AZ", input.acceleration(Dimension.Z)))
loops.every_interval(1000, on_every_interval)


# tie it on the back of a hand then do a high five to measure the speed and acceleration of the high five