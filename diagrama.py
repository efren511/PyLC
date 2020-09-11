#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from termcolor import colored
import time
def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(40, GPIO.IN)
    GPIO.setup(37, GPIO.OUT)
    while True:
        contacto40 = GPIO.input(40)
        if contacto40:
            GPIO.output(37, GPIO.HIGH)
        else:
            GPIO.output(37, GPIO.LOW)
if __name__ == '__main__':
    try:
        print(colored('''----------ENTRADAS-----------
Entrada en el pin (40)
-----------------------------

----------SALIDAS----------
Salida en el pin (37)
-----------------------------
   40      37   
--| |----( )--
''', "yellow"))
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit("Bye bye")
