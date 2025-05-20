from time import time,sleep
import RPi.GPIO as GPIO
delay=.1
inPin=40
outPin=38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPin,GPIO.OUT)
GPIO.setup(inPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
mode=0
buttonstate=1
buttonstateold=1
light=False
last_toggle_time=time()
try:
        while True:
                buttonstate=GPIO.input(inPin)
                if buttonstate==1 and buttonstateold==0:
                        mode=(mode+1)%4
                        if mode==0:
                                GPIO.output(outPin,GPIO.LOW)
                        elif mode==1:
                                GPIO.output(outPin,GPIO.HIGH)
                        elif mode in [2,3]:
                                light=True
                                last_toggle_time=time()
                if mode==2:
                  if time()-last_toggle_time>=1:
                                light= not light
                                GPIO.output(outPin,light)
                                last_toggle_time=time()
                elif mode==3:
                        if time()-last_toggle_time>=0.2:
                                light= not light
                                GPIO.output(outPin,light)
                                last_toggle_time=time()
                buttonstateold=buttonstate
                sleep(0.05)
except KeyboardInterrupt:
        GPIO.cleanup()
