#!/usr/bin/env python3
## -*- coding: utf-8 -*-

#importamos el modulo para trabajar con los pines
import RPi.GPIO as GPIO
#importamos modulo para trabajar con pausas
import time

#creamos la funcion principal
def main():
    #ponemos los pines en modo board
    GPIO.setmode(GPIO.BOARD)
    #declaramos el pin como salida
    GPIO.setup(37, GPIO.OUT)
    #creamos un bucle infinito
    while True:
        #encendemos pin 3
        GPIO.output(37, GPIO.HIGH)
        #esperamos 1 segundo
        time.sleep(1)
        #apagamos pin 3
        GPIO.output(37, GPIO.LOW)
        #esperamos 1 segundo
        time.sleep(1)

#llamamos a la funcion principal
if __name__ == '__main__':
    #tratamos de llamar a la funcion principal
    try:
        #llamamos a la funcion principal
        main()
    #si detectamos tecla de salida
    except KeyboardInterrupt:
        #limpiamos los ajustes
        GPIO.cleanup()
        #salimos de la ejecucion general
        exit("Bye bye")
