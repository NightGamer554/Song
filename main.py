from machine import Pin, PWM, ADC
from time import sleep

white = Pin(20, Pin.OUT)
red = Pin(19, Pin.OUT)
blue = Pin(18, Pin.OUT)
yellow = Pin(17, Pin.OUT)
green = Pin(16, Pin.OUT)

buzzer = PWM(Pin(21))
button1 = Pin(28, Pin.IN)

# test script



def noSong():
   print("off")
   
def song():
    print("song")

    while True:

     green.on()
     sleep(0.1)
     buzzer.freq(2000) # note
     buzzer.duty_u16(500)# volume
     yellow.on()
     white.off()
     sleep(0.1)
     blue.on()
     buzzer.freq(650)
     buzzer.duty_u16(500)
     green.off()
     sleep(0.1)
     red.on()
     yellow.off()
     sleep(0.1)
     white.on()
     buzzer.freq(320)
     buzzer.duty_u16(500)
     blue.off()
     sleep(0.1)
     red.off()
    

if button1.value() == True:
   song()

song()


# def NoSong():
#     pass

# def Song():
#     pass

