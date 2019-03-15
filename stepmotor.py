
'''
All imports
'''
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


'''
Pin Connection for Motor 1
'''
A = 7
B = 11
C = 13
D = 15
'''
Pin Connection for Motor 2
'''
E = 8
F = 12
G = 18
H = 16

GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)



GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(H, GPIO.OUT)


"""
      1  2  3  4  5  6  7  8
      
Pin1  x  x                 x
Pin2     x  x  x
Pin3           x  x  x
Pin4                 x  x  x

"""

def GPIO_SETUP_1(a,b,c,d):
    GPIO.output(A, a)
    GPIO.output(B, b)
    GPIO.output(C, c)
    GPIO.output(D, d)
    time.sleep(0.001)


def GPIO_SETUP_2(e,f,g,h):
    GPIO.output(E, e)
    GPIO.output(F, f)
    GPIO.output(G, g)
    GPIO.output(H, h)
    time.sleep(0.001)

def RIGHT_TURN_1(deg):

    full_circle = 510.0
    degree = full_circle/360*deg
    GPIO_SETUP_1(0,0,0,0)

    while degree > 0.0:
        GPIO_SETUP_1(1,0,0,0)
        GPIO_SETUP_1(1,1,0,0)
        GPIO_SETUP_1(0,1,0,0)
        GPIO_SETUP_1(0,1,1,0)
        GPIO_SETUP_1(0,0,1,0)
        GPIO_SETUP_1(0,0,1,1)
        GPIO_SETUP_1(0,0,0,1)
        GPIO_SETUP_1(1,0,0,1)
        degree -= 1

def LEFT_TURN_1(deg):

    full_circle = 510.0
    degree = full_circle/360*deg
    GPIO_SETUP_1(0,0,0,0)

    while degree > 0.0:
        GPIO_SETUP_1(1,0,0,1)
        GPIO_SETUP_1(0,0,0,1)
        GPIO_SETUP_1(0,0,1,1)
        GPIO_SETUP_1(0,0,1,0)
        GPIO_SETUP_1(0,1,1,0)
        GPIO_SETUP_1(0,1,0,0)
        GPIO_SETUP_1(1,1,0,0)
        GPIO_SETUP_1(1,0,0,0)
        degree -= 1


def RIGHT_TURN_2(deg):

    full_circle = 510.0
    degree = full_circle/360*deg
    GPIO_SETUP_2(0,0,0,0)

    while degree > 0.0:
        GPIO_SETUP_2(1,0,0,0)
        GPIO_SETUP_2(1,1,0,0)
        GPIO_SETUP_2(0,1,0,0)
        GPIO_SETUP_2(0,1,1,0)
        GPIO_SETUP_2(0,0,1,0)
        GPIO_SETUP_2(0,0,1,1)
        GPIO_SETUP_2(0,0,0,1)
        GPIO_SETUP_2(1,0,0,1)
        degree -= 1

def LEFT_TURN_2(deg):

    full_circle = 510.0
    degree = full_circle/360*deg
    GPIO_SETUP_2(0,0,0,0)

    while degree > 0.0:
        GPIO_SETUP_2(1,0,0,1)
        GPIO_SETUP_2(0,0,0,1)
        GPIO_SETUP_2(0,0,1,1)
        GPIO_SETUP_2(0,0,1,0)
        GPIO_SETUP_2(0,1,1,0)
        GPIO_SETUP_2(0,1,0,0)
        GPIO_SETUP_2(1,1,0,0)
        GPIO_SETUP_2(1,0,0,0)
        degree -= 1

#MAIN #########################


RIGHT_TURN_1(90)
time.sleep(10)
LEFT_TURN_1(90)
GPIO_SETUP_1(0,0,0,0)


RIGHT_TURN_2(90)
time.sleep(10)
LEFT_TURN_2(90)
GPIO_SETUP_2(0,0,0,0)
    

