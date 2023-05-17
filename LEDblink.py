from machine import Pin
from time import sleep
myLED=('LED', pin.OUT)
while True:
    myLED.value(1) # 1 = on, 0 = off; could all do myLED.on/myLED.off
    sleep(1) # pause between blinks
    myLED.value(0)
    sleep(1)
    
    
