#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from termcolor import colored

#menu principal
menu = """
1) -| |-
2) -|/|-
3) -( )-
4) -(fin)-"""

#declaramos una funcion para escribir un txt
def escribir(elemento):
    #abrimos un archivo para escribir
    with open("diagrama.txt", "a") as f:
        #escribimos en el archivo
        f.write(elemento)
    #abrimos un archivo para leer
    with open("diagrama.txt", "r") as f:
        #mostramos el contenido del archivo
        print(f.read())

#creamos una funcion principal
def main():
    #cremos un bucle para solicitar componentes
    while True:
        #mostramos el menu
        print(colored(menu, "green"))
        #solicitamos el componente a usar
        componente = input("Seleccione un componente: ")
        #si el usuario usa la opcion 4
        if componente == "4":
            #salimos
            exit("Bye bye")
        #y si no...
        else:
            #si el componente es 1
            if componente == "1":
                escribir("-| |-")
            #si el componente es 2
            elif componente == "2":
                escribir("-|/|-")
            #si el componente es 3
            elif componente == "3":
                escribir("-( )-\n")

#creamos un punto de acceso
if __name__ == '__main__':
    #llamamos a la funcion principal
    main()
