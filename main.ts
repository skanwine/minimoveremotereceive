function moveFront() {
    
    move = "Front"
    pins.servoWritePin(AnalogPin.P1, 0)
    pins.servoWritePin(AnalogPin.P2, 180)
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    moveFront()
})
function moveBack() {
    
    move = "Back"
    pins.servoWritePin(AnalogPin.P1, 180)
    pins.servoWritePin(AnalogPin.P2, 0)
}

function moveNo() {
    
    move = "No"
    pins.servoWritePin(AnalogPin.P1, 90)
    pins.servoWritePin(AnalogPin.P2, 90)
}

input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    moveNo()
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    if (receivedString == "A") {
        moveFront()
    } else if (receivedString == "B") {
        moveBack()
    } else if (receivedString == "AB") {
        moveNo()
    } else if (receivedString == "L") {
        Pixel_Array.clear()
        Pixel_Array.setPixelColor(0, neopixel.colors(NeoPixelColors.Yellow))
        Pixel_Array.setPixelColor(1, neopixel.colors(NeoPixelColors.Yellow))
        Pixel_Array.show()
        pins.servoWritePin(AnalogPin.P1, 0)
        pins.servoWritePin(AnalogPin.P2, 90)
        basic.pause(300)
        pins.servoWritePin(AnalogPin.P1, 90)
        if (move == "Front") {
            moveFront()
        } else if (move == "Back") {
            moveBack()
        } else if (move == "No") {
            moveNo()
        }
        
    } else if (receivedString == "R") {
        Pixel_Array.clear()
        Pixel_Array.setPixelColor(3, neopixel.colors(NeoPixelColors.Yellow))
        Pixel_Array.setPixelColor(4, neopixel.colors(NeoPixelColors.Yellow))
        Pixel_Array.show()
        pins.servoWritePin(AnalogPin.P1, 90)
        pins.servoWritePin(AnalogPin.P2, 180)
        basic.pause(300)
        pins.servoWritePin(AnalogPin.P2, 90)
        if (move == "Front") {
            moveFront()
        } else if (move == "Back") {
            moveBack()
        } else if (move == "No") {
            moveNo()
        }
        
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    moveBack()
})
let move = ""
let Pixel_Array : neopixel.Strip = null
Pixel_Array = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
Pixel_Array.setBrightness(30)
radio.setGroup(18)
move = "No"
basic.showIcon(IconNames.Heart)
basic.forever(function on_forever() {
    if (move == "No") {
        Pixel_Array.clear()
        Pixel_Array.show()
        basic.pause(200)
        Pixel_Array.setPixelColor(0, neopixel.colors(NeoPixelColors.Yellow))
        Pixel_Array.setPixelColor(1, neopixel.colors(NeoPixelColors.Yellow))
        Pixel_Array.setPixelColor(3, neopixel.colors(NeoPixelColors.Yellow))
        Pixel_Array.setPixelColor(4, neopixel.colors(NeoPixelColors.Yellow))
        Pixel_Array.show()
        basic.pause(200)
    } else if (move == "Back") {
        Pixel_Array.setPixelColor(0, neopixel.colors(NeoPixelColors.Blue))
        Pixel_Array.setPixelColor(1, neopixel.colors(NeoPixelColors.Green))
        Pixel_Array.setPixelColor(2, neopixel.colors(NeoPixelColors.Yellow))
        Pixel_Array.setPixelColor(3, neopixel.colors(NeoPixelColors.Orange))
        Pixel_Array.setPixelColor(4, neopixel.colors(NeoPixelColors.Red))
        Pixel_Array.show()
    } else if (move == "Front") {
        Pixel_Array.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
        Pixel_Array.setPixelColor(1, neopixel.colors(NeoPixelColors.Orange))
        Pixel_Array.setPixelColor(2, neopixel.colors(NeoPixelColors.Yellow))
        Pixel_Array.setPixelColor(3, neopixel.colors(NeoPixelColors.Green))
        Pixel_Array.setPixelColor(4, neopixel.colors(NeoPixelColors.Blue))
        Pixel_Array.show()
    } else {
        
    }
    
})
