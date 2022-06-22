radio.onReceivedString(function (receivedString) {
    if (receivedString == "A") {
        maqueen.MotorRun(maqueen.aMotors.M1, maqueen.Dir.CW, 200)
        maqueen.MotorRun(maqueen.aMotors.M2, maqueen.Dir.CW, 200)
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
    }
    if (receivedString == "R") {
        maqueen.MotorRun(maqueen.aMotors.M1, maqueen.Dir.CCW, 200)
        maqueen.MotorRun(maqueen.aMotors.M2, maqueen.Dir.CCW, 200)
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
    }
    if (receivedString == "G") {
        maqueen.MotorRun(maqueen.aMotors.M1, maqueen.Dir.CW, 50)
        maqueen.MotorRun(maqueen.aMotors.M2, maqueen.Dir.CW, 200)
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
    }
    if (receivedString == "D") {
        maqueen.MotorRun(maqueen.aMotors.M1, maqueen.Dir.CW, 200)
        maqueen.MotorRun(maqueen.aMotors.M2, maqueen.Dir.CW, 50)
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
    }
    if (receivedString == "B") {
        maqueen.motorStopAll()
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
    }
    if (receivedString == "J") {
        music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
    }
    if (receivedString == "BB") {
        maqueen.MotorRun(maqueen.aMotors.M1, maqueen.Dir.CW, 200)
        maqueen.MotorRun(maqueen.aMotors.M2, maqueen.Dir.CCW, 200)
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
    }
    if (receivedString == "BA") {
        maqueen.MotorRun(maqueen.aMotors.M1, maqueen.Dir.CCW, 200)
        maqueen.MotorRun(maqueen.aMotors.M2, maqueen.Dir.CW, 200)
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
    }
})
radio.setGroup(1)
let strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Blue))
let cpt = 1
basic.forever(function () {
    if (maqueen.sensor(PingUnit.Centimeters) < 20 && maqueen.sensor(PingUnit.Centimeters) != 0) {
        cpt += 1
        if (cpt == 5) {
            maqueen.motorStopAll()
            radio.sendString("X")
            music.playTone(988, music.beat(BeatFraction.Whole))
            basic.pause(1000)
            music.playTone(988, music.beat(BeatFraction.Whole))
            basic.pause(1000)
            music.playTone(988, music.beat(BeatFraction.Whole))
            basic.pause(1000)
            cpt = 1
        }
    } else {
        cpt = 1
    }
})
