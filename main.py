def moveFront():
    global move
    move = "Front"
    pins.servo_write_pin(AnalogPin.P1, 0)
    pins.servo_write_pin(AnalogPin.P2, 180)

def on_button_pressed_a():
    moveFront()
input.on_button_pressed(Button.A, on_button_pressed_a)

def moveBack():
    global move
    move = "Back"
    pins.servo_write_pin(AnalogPin.P1, 180)
    pins.servo_write_pin(AnalogPin.P2, 0)
def moveNo():
    global move
    move = "No"
    pins.servo_write_pin(AnalogPin.P1, 90)
    pins.servo_write_pin(AnalogPin.P2, 90)

def on_button_pressed_ab():
    moveNo()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    if receivedString == "A":
        moveFront()
    elif receivedString == "B":
        moveBack()
    elif receivedString == "AB":
        moveNo()
    elif receivedString == "L":
        Pixel_Array.clear()
        Pixel_Array.set_pixel_color(0, neopixel.colors(NeoPixelColors.YELLOW))
        Pixel_Array.set_pixel_color(1, neopixel.colors(NeoPixelColors.YELLOW))
        Pixel_Array.show()
        pins.servo_write_pin(AnalogPin.P1, 0)
        pins.servo_write_pin(AnalogPin.P2, 90)
        basic.pause(300)
        pins.servo_write_pin(AnalogPin.P1, 90)
        if move == "Front":
            moveFront()
        elif move == "Back":
            moveBack()
        elif move == "No":
            moveNo()
    elif receivedString == "R":
        Pixel_Array.clear()
        Pixel_Array.set_pixel_color(3, neopixel.colors(NeoPixelColors.YELLOW))
        Pixel_Array.set_pixel_color(4, neopixel.colors(NeoPixelColors.YELLOW))
        Pixel_Array.show()
        pins.servo_write_pin(AnalogPin.P1, 90)
        pins.servo_write_pin(AnalogPin.P2, 180)
        basic.pause(300)
        pins.servo_write_pin(AnalogPin.P2, 90)
        if move == "Front":
            moveFront()
        elif move == "Back":
            moveBack()
        elif move == "No":
            moveNo()
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    moveBack()
input.on_button_pressed(Button.B, on_button_pressed_b)

move = ""
Pixel_Array: neopixel.Strip = None
Pixel_Array = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
Pixel_Array.set_brightness(30)
radio.set_group(18)
move = "No"
basic.show_icon(IconNames.HEART)

def on_forever():
    if move == "No":
        Pixel_Array.clear()
        Pixel_Array.show()
        basic.pause(200)
        Pixel_Array.set_pixel_color(0, neopixel.colors(NeoPixelColors.YELLOW))
        Pixel_Array.set_pixel_color(1, neopixel.colors(NeoPixelColors.YELLOW))
        Pixel_Array.set_pixel_color(3, neopixel.colors(NeoPixelColors.YELLOW))
        Pixel_Array.set_pixel_color(4, neopixel.colors(NeoPixelColors.YELLOW))
        Pixel_Array.show()
        basic.pause(200)
    elif move == "Back":
        Pixel_Array.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLUE))
        Pixel_Array.set_pixel_color(1, neopixel.colors(NeoPixelColors.GREEN))
        Pixel_Array.set_pixel_color(2, neopixel.colors(NeoPixelColors.YELLOW))
        Pixel_Array.set_pixel_color(3, neopixel.colors(NeoPixelColors.ORANGE))
        Pixel_Array.set_pixel_color(4, neopixel.colors(NeoPixelColors.RED))
        Pixel_Array.show()
    elif move == "Front":
        Pixel_Array.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
        Pixel_Array.set_pixel_color(1, neopixel.colors(NeoPixelColors.ORANGE))
        Pixel_Array.set_pixel_color(2, neopixel.colors(NeoPixelColors.YELLOW))
        Pixel_Array.set_pixel_color(3, neopixel.colors(NeoPixelColors.GREEN))
        Pixel_Array.set_pixel_color(4, neopixel.colors(NeoPixelColors.BLUE))
        Pixel_Array.show()
    else:
        pass
basic.forever(on_forever)
