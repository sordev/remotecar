import RPi.GPIO as GPIO
import pygame, sys, time
from pygame.locals import *
from time import sleep

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
 
GPIO.setmode(GPIO.BOARD)

interval = 0.2
 
#yellow in1
Motor1A = 16
#orange in2
Motor1B = 18
#Brown en1
Motor1E = 22

#green - in4
Motor2A = 11
#blue - in3
Motor2B = 13
#grape - en2
Motor2E = 15

#setup 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

def bw():
	print "Going forwards"
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
	return

def fw():
	print "Going backwards"
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
	return

def tl():
	print "Going left"
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)	
	
	return

def tr():
	print "Going right"
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)		
	return

def stop():
	print "Stop"
	GPIO.output(Motor2E,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.LOW)

# tester('axis',False)
# axis 0 ->left right 1 -0.99
# axis 12 ->l analog 0.99 
# axis 13 ->r analog 0.99
"""
0 = Left joystick left to right values -1.0 to 0.99
1 = Left joystick up to down values -1.0 to 0.99
2 = Right joystick left to right values -1.0 to 0.99
3 = Right joystick up to down values -1.0 to 0.99

0 = Select
1 =
2 = 
3 = Start
4 = Digital Up
5 = Digital Right
6 = Digital Down
7 = Digitial Left
8 = L2 (digital mode)
9 = R2 (digital mode)
10 = R1
11 = L1
12 = Triangle
13 = Circle
14 = X
15 = Square
16 = PS
17 = 
18 =


GPIO.output(Motor2E,GPIO.LOW)
GPIO.output(Motor1E,GPIO.LOW)
GPIO.cleanup()
"""
while True:
	
	pygame.event.pump()
	lr = joystick.get_axis(0)
	acc = joystick.get_axis(12)
	rev = joystick.get_axis(13)
	start = joystick.get_button(3)
	
	if lr > 0.2:
		tr()
		sleep(interval)
	elif lr < -0.2:
		tl()
		sleep(interval)
	elif lr < 0.2 and lr > -0.2  :
		#sleep(interval)
		stop()
		
	if acc > 0.2:
		fw()
		sleep(interval)
	elif acc < 0.2:
		stop()
		
	if rev > 0.2:
		bw()
		sleep(interval)
	elif rev < 0.2:
		stop()
	
	if start == 1:
		stop()
		GPIO.output(Motor2E,GPIO.LOW)
		GPIO.output(Motor1E,GPIO.LOW)
		GPIO.cleanup()
		exit()
		
	print lr + acc + rev
	
	#sleep(interval)
	
GPIO.cleanup()
