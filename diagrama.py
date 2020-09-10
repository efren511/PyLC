
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(1, GPIO.IN)
    GPIO.setup(2, GPIO.IN)
    GPIO.setup(3, GPIO.IN)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(1, GPIO.IN)
    GPIO.setup(2, GPIO.IN)
    GPIO.setup(3, GPIO.IN)
    GPIO.setup(1, GPIO.OUT)
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
