from machine import Pin, PWM
from time import sleep
# strftime("%Y-%m-%d %H:%M:%S", gmtime())

led = Pin("LED",Pin.OUT)

#set PWM
pwm = PWM(Pin(21)) 
pwm.freq(50) #20ms PWM period

rtc = machine.RTC()

led.off()

def blinker():
    count=5
    while count > 0:
        led.toggle()
        print("LED ON {}".format(count))
        sleep(.25)
        led.toggle()
        count=count-1
        sleep(.25)
    
blinker()

while True:
    led.on()
    print(rtc.datetime())
    pwm.duty_ns(1500000) #middle
    sleep(.5)
    led.off()
    sleep(2)  #####here is the wait
    led.on()
    print(rtc.datetime())
    pwm.duty_ns(2050000) #this is OFF
    sleep(.5)
    led.off()
    sleep(.5)
    led.on()
    print(rtc.datetime())
    pwm.duty_ns(1500000)
    sleep(.5)
    led.off()
    sleep(2)  #####here is the wait
    led.on()
    print(rtc.datetime())
    pwm.duty_ns(1000000) #this is ON
    sleep(.5)
    led.off()
    sleep(.5)

