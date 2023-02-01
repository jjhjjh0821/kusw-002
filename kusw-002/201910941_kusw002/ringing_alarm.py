
# coding: utf-8

# In[ ]:


import pygame
import RPi.GPIO as GPIO
import time

#GPIO.setwarning(False)
GPIO.setmode(GPIO.BCM)

RED = 14
GREEN = 15
BLUE = 18

GPIO.setup(RED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GREEN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BLUE, GPIO.OUT, initial=GPIO.LOW)

def select_alarm(result) :
    if result == 0 :
        sound_alarm("power_alarm.wav")
        #led off
        GPIO.setup(GREEN, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(BLUE, GPIO.OUT, initial=GPIO.LOW)
        try:
            while 1:
                GPIO.output(RED, GPIO.HIGH)
                time.sleep(0.5)
                #GPIO.output(RED, GPIO.LOW)
                #time.sleep(0.5)
        except KeyboardInterrupt:
            pass
            
        GPIO.cleanup()
        
    elif result == 1 :
        sound_alarm("nomal_alarm.wav")
        #led off
        GPIO.setup(RED, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(BLUE, GPIO.OUT, initial=GPIO.LOW)
        try:
            while 1:
                GPIO.output(GREEN, GPIO.HIGH)
                time.sleep(0.5)
                #GPIO.output(GREEN, GPIO.LOW)
                #time.sleep(0.5)

        except KeyboardInterrupt:
            pass
            
        GPIO.cleanup()
        
    else :
        sound_alarm("short_alarm.mp3")
        #led off
        GPIO.setup(RED, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(GREEN, GPIO.OUT, initial=GPIO.LOW)
        try:
            while 1 :
                GPIO.output(BLUE, GPIO.HIGH)
                time.sleep(0.5)
                #GPIO.output(BLUE, GPIO.LOW)
                #time.sleep(0.5)
                
        except KeyboardInterrupt:
            pass
	
        GPIO.cleanup()

def sound_alarm(path) :
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    

