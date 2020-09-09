#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#importamos el modulo para trabajar con colores
from termcolor import colored

#menu principal
menu1 = """1) Crear Ladder
2) Subir Ladder
3) Ayuda
4) Salir\n"""

#menu secundario
menu2 = """
1) -| |-
2) -|/|-
3) -( )-\n"""

#declaramos una funcion para escribir un txt
def escribir(elemento):
    #abrimos un archivo para escribir
    with open("diagrama.txt", "a") as f:
        #escribimos en el archivo
        f.write(elemento)
    #abrimos un archivo para leer
    with open("diagrama.txt", "r") as f:
        #mostramos el contenido del archivo
        print(colored(f.read(), "yellow"))

#creamos una funcion principal
def main():
    #creamos un bucle para solicitar la opcion para trabajar
    while True:
        #mostramos el menu principal
        print(colored(menu1, "green"))
        #solicitamos el modo de trabajo
        modo = input("Ingresa el modo de trabajo: ")
        #si el modo es 1
        if modo == "1":
            #llamamos a la funcion...
            crear()
        #y si no...
        else:
            #mostramos un mensaje de error
            print(colored("Modo Desconocido!", "red"))
#creamos una funcion para realizar el ladder
def crear():
    #creamos una variable para saber si se esta editando el diagrama
    edicion = True
    #creamos un bucle para que este solicitando los elementos correspondientes
    while edicion:
        #creamos una lista para almacenar los pines
        pines = []
        #creamos un bucle para solicitar el numero de los pines
        while True:
            #solicitamos los pines a usar
            pin = input(colored("Ingresa:\nPin a usar\n'Enter' para la siguiente linea\n'exit' para terminar\n#: ", "blue"))
            #si el usuario no escribio nada
            if pin == "" or pin == "exit":
                #escribimos un salto de linea
                escribir("\n")
                #salimos del bucle
                break
            else:
                #escribimos en el diagrama el pin
                escribir("   {}   ".format(pin))
                #agregamos el pin a la lista
                pines.append(pin)
                #cremos un bucle para solicitar componentes
        for pin in pines:
            #mostramos el menu
            print(colored(menu2, "green"))
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
                    #escribimos...
                    escribir("--| |--")
                    #si el componente es 2
                elif componente == "2":
                    #escribimos...
                    escribir("--|/|--")
                    #si el componente es 3
                elif componente == "3":
                    #escribimos...
                    escribir("--( )--\n")
                    #y si no
                else:
                    #mostramos un error
                    print(colored("Componente Desconocido!!", "red"))
#creamos un punto de acceso
if __name__ == '__main__':
    #llamamos a la funcion principal
    main()
