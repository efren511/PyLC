#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#importamos el modulo para trabajar con los pines
import RPi.GPIO as GPIO
#importamos modulo para trabajar con pausas
import time

#creamos la funcion principal
def main():
    #ajustamos los pines a modo board
    GPIO.setmode(GPIO.BOARD)
    #ajustamos el pin de entrada
    GPIO.setup(40, GPIO.IN)
    #ajustamos el pin de salida
    GPIO.setup(37, GPIO.OUT)
    while True:
        #leemos el boton
        boton = GPIO.input(40)
        #si el boton esta desactivado
        if boton == False:
            #apagamos el led
            GPIO.output(37, GPIO.HIGH)
        #y si no
        else:
            #encendemos el led
            GPIO.output(37, GPIO.LOW)

#creamos un punto de acceso
if __name__ == '__main__':
    try:
        #llamamos a la funcion principal
        main()
    except KeyboardInterrupt:
         #limpiamos los ajustes
         GPIO.cleanup()
         #salimos de la ejecucion general
         exit("Bye bye")
