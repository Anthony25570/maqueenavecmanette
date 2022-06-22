def on_received_string(receivedString):
    if receivedString == "A":
        maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 200)
        maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 200)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
    if receivedString == "R":
        maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CCW, 200)
        maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CCW, 200)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
    if receivedString == "G":
        maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 50)
        maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 200)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
    if receivedString == "D":
        maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 200)
        maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 50)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
    if receivedString == "B":
        maqueen.motor_stop_all()
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
    if receivedString == "J":
        music.start_melody(music.built_in_melody(Melodies.DADADADUM),
            MelodyOptions.ONCE)
    if receivedString == "BB":
        maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 200)
        maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CCW, 200)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
    if receivedString == "BA":
        maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CCW, 200)
        maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 200)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
radio.on_received_string(on_received_string)

radio.set_group(1)
strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
cpt = 1

def on_forever():
    global cpt
    if maqueen.sensor(PingUnit.CENTIMETERS) < 20 and maqueen.sensor(PingUnit.CENTIMETERS) != 0:
        cpt += 1
        if cpt == 5:
            maqueen.motor_stop_all()
            radio.send_string("X")
            music.play_tone(988, music.beat(BeatFraction.WHOLE))
            basic.pause(1000)
            music.play_tone(988, music.beat(BeatFraction.WHOLE))
            basic.pause(1000)
            music.play_tone(988, music.beat(BeatFraction.WHOLE))
            basic.pause(1000)
            cpt = 1
    else:
        cpt = 1
basic.forever(on_forever)
