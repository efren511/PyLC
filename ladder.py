#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from termcolor import colored
import time
def run(diagrama):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.IN)
    GPIO.setup(40, GPIO.OUT)
    print(diagrama)
    try:
        while True:
        contacto37 = GPIO.input(37)
        if contacto37:
            GPIO.output(40, GPIO.HIGH)
        else:
            GPIO.output(40, GPIO.LOW)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit("Bye bye")
