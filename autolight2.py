from machine import Pin, PWM
from time import sleep
# strftime("%Y-%m-%d %H:%M:%S", gmtime())

led = Pin("LED",Pin.OUT)

#set PWM
pwm = PWM(Pin(21)) 
pwm.freq(50) #20ms PWM period

rtc = machine.RTC()

second=1
minute=60
hour=60*minute
day=24*hour
week=7*day

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

def ledfade(hr):
    for z in range(hr):
        led.on()
        sleep(2)
        led.off()
        sleep(10)
#ledfade()

downtime=8*hour
print(downtime)
def winddown(hr):
    for x in range(hr):
        print(f'Sleeping... {x}')
        ledfade(hr)
#winddown(downtime)

def snooze():
    for y in range(24*hour):
        print(f'Snoozing...{24-y} hour left')
        ledfade(1*hour)
#snooze()
        
def onlight():
    print('light on')
    led.on()
    print(rtc.datetime())
    pwm.duty_ns(1500000) #middle
    sleep(1)
    pwm.duty_ns(1000000) #this is ON
    sleep(1)
    pwm.duty_ns(1500000) #middle
    led.off()
    
def offlight():
    print('light off')
    led.on()
    print(rtc.datetime())
    pwm.duty_ns(1500000) #middle
    sleep(1)
    pwm.duty_ns(2050000) #this is OFF
    sleep(1)
    pwm.duty_ns(1500000) #middle
    led.off()

#####################
    
winddown(downtime) 
for d in range(5): #testing for first 5 days
    onlight()
    snooze()

#####################
'''
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
'''