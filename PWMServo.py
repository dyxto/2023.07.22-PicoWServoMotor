from machine import Pin, PWM
import time
import network
import BlynkLib

led = Pin("LED",Pin.OUT)

#set PWM
pwm = PWM(Pin(21)) 
pwm.freq(50) #20ms PWM period

from secret import ssid, password, blynk

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid,password)
 
BLYNK_AUTH = blynk
 

# connect the network       
wait = 5
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(.2)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
    if wlan.status() != 3:
        led.off()
else:
    print('connected')
    if wlan.status() == 3:
        led.on()
    ip=wlan.ifconfig()[0]
    print('IP: ', ip)

 
"Connection to Blynk"
# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)
 
# Register virtual pin handler
@blynk.on("V0") #virtual pin V0
def v0_write_handler(value): #read the value
    if int(value[0]) == 1:
        print("RIGHT")
        pwm.duty_ns(2050000) #dutyCycle 2ms
        time.sleep(1)
    if int(value[0]) != 1:
        print("LEFT")
        pwm.duty_ns(1000000) #dutyCycle .5ms
        time.sleep(1)

# Register virtual pin handler
@blynk.on("V4") #virtual pin V0
def v4_write_handler(value): #read the value
    if int(value[0]) == 1:
        print("SPIN ON")
    else:
        print("SPIN OFF")
        pwm.deinit()
        
while True:
    blynk.run()
    pwm.duty_ns(1500000) #dutyCycle 2ms
    time.sleep(1)
