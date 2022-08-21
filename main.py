from machine import Pin
import time

ledSnooze = 18
ledPin1 = 19
ledPin2 = 20
ledPin3 = 21
ledPin4 = 22

btnPin1 = 9
btnPin2 = 8
btnPin3 = 11
btnPin4 = 12
btnPin5 = 13

ledSnooze = Pin(ledSnooze, Pin.OUT)
led1 = Pin(ledPin1, Pin.OUT)
led2 = Pin(ledPin2, Pin.OUT)
led3 = Pin(ledPin3, Pin.OUT)
led4 = Pin(ledPin4, Pin.OUT)

btnSnooze = Pin(btnPin1, Pin.IN, Pin.PULL_UP)
btn1 = Pin(btnPin2, Pin.IN, Pin.PULL_UP)
btn2 = Pin(btnPin3, Pin.IN, Pin.PULL_UP)
btn3 = Pin(btnPin4, Pin.IN, Pin.PULL_UP)
btn4 = Pin(btnPin5, Pin.IN, Pin.PULL_UP)
    
waitTime = 60 * 60 * 4
snoozeTime = 60 * 60 * 12

snoozeLastTimePressed = time.ticks_ms() - (snoozeTime * 1000)
task1LastTimePressed = time.ticks_ms() - (waitTime * 1000)
task2LastTimePressed = time.ticks_ms() - (waitTime * 1000)
task3LastTimePressed = time.ticks_ms() - (waitTime * 1000)
task4LastTimePressed = time.ticks_ms() - (waitTime * 1000)
    
def getButton(btn):
    return not btn.value()

while True:
    if time.ticks_diff(time.ticks_ms(), snoozeLastTimePressed) / 1000 < snoozeTime:
        ledSnooze.value(0)
        led1.value(0)
        led2.value(0)
        led3.value(0)
        led4.value(0)
        continue
    else:
        ledSnooze.value(1)
    
    if getButton(btnSnooze):
        print("btnSnooze pressed")
        snoozeLastTimePressed = time.ticks_ms()
        
    if getButton(btn1):
        print("btn1 pressed")
        task1LastTimePressed = time.ticks_ms()
        
    if getButton(btn2):
        print("btn2 pressed")
        task2LastTimePressed = time.ticks_ms()
        
    if getButton(btn3):
        print("btn4 pressed")
        task3LastTimePressed = time.ticks_ms()
        
    if getButton(btn4):
        print("btn5 pressed")
        task4LastTimePressed = time.ticks_ms()
        
    if time.ticks_diff(time.ticks_ms(), task1LastTimePressed) / 1000 > waitTime:
        led1.value(1)
    else:
        led1.value(0)
        
    if time.ticks_diff(time.ticks_ms(), task2LastTimePressed) / 1000 > waitTime:
        led2.value(1)
    else:
        led2.value(0)
        
    if time.ticks_diff(time.ticks_ms(), task3LastTimePressed) / 1000 > waitTime:
        led3.value(1)
    else:
        led3.value(0)
        
    if time.ticks_diff(time.ticks_ms(), task4LastTimePressed) / 1000 > waitTime:
        led4.value(1)
    else:
        led4.value(0)
        
    time.sleep(0.1)
    