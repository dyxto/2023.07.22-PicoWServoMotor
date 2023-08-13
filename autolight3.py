#thought of this at work lol (7/24/23)
from machine import Pin, PWM
from time import sleep

led = Pin("LED",Pin.OUT)
led.off()

#set PWM
pwm = PWM(Pin(21)) 
pwm.freq(50) #20ms PWM period

#defining amount of time in seconds
second=1
minute=60*second
hour=60*minute
day=24*hour
weekday=5*day
week=7*day

def onlight():
    led.on()
    print('light is on')
    pwm.duty_ns(1500000) #middle
    sleep(.5)
    pwm.duty_ns(1000000) #this is ON
    sleep(.5)
    pwm.duty_ns(1500000) #middle
    led.off()
    sleep(1)
    
def offlight():
    led.on()
    print('light is off')
    pwm.duty_ns(1500000) #middle
    sleep(.5)
    pwm.duty_ns(2100000) #this is ON
    sleep(.5)
    pwm.duty_ns(1500000) #middle
    led.off()
    sleep(1)
    
def snooze(timer):
    print('snoozzzzzzzzing')
    for x in range(timer):
        print(f'ZZZZzzzz...{x+1}')
        led.on()
        sleep(.5)
        led.off()
        sleep(.5)
        
#######################################
        
#snooze(10) 		#countdown to alarm
while True: 	#the infinite loop starts
    onlight()
    offlight()
    snooze(24*hour)	#repeat at this time (24 hours)
    