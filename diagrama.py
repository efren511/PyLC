#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(1, GPIO.IN)
    GPIO.setup(2, GPIO.IN)
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)
    while True:
        contacto1 = GPIO.input(1)
        contacto2 = GPIO.input(2)
        if contacto1 and not contacto2:
            GPIO.output(3, GPIO.LOW)
        else:
            GPIO.output(3, GPIO.HIGH)
        if not contacto1 and not contacto2:
            GPIO.output(4, GPIO.LOW)
        else:
            GPIO.output(4, GPIO.HIGH)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
         GPIO.cleanup()
         exit("Bye bye")
