let IsLogging = false
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    datalogger.deleteLog()
    IsLogging = true
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    IsLogging = false
})
loops.everyInterval(1000, function on_every_interval() {
    if (IsLogging) {
        basic.showIcon(IconNames.SmallDiamond)
        basic.clearScreen()
        datalogger.log(datalogger.createCV("AX", input.acceleration(Dimension.X)), datalogger.createCV("AY", input.acceleration(Dimension.Y)), datalogger.createCV("AZ", input.acceleration(Dimension.Z)))
    }
    
})
