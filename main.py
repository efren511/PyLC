#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#importamos el modulo para trabajar con colores
from termcolor import colored
#importamos modulo para trabajar con comandos del sistema
import subprocess

#creamos una variable para los ajustes
ajustes = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from termcolor import colored
import time\n"""

#creamos una variable para el inicio del codigo
inicio = """def main():
    GPIO.setmode(GPIO.BOARD)\n"""

bucle = """    while True:\n"""

#menu principal
menu1 = """1) Crear Ladder
2) Subir Ladder
3) Ayuda
4) Salir\n"""

#menu secundario
menu2 = """
1) -| |-\n
2) -|/|-\n
3) -( )-\n"""

#creamos una funcion para mostrar el diagrama
def mostrar():
    #limpiamos la pantalla
    limpiar()
    #mostramos el contenido del archivo
    print(colored(diagrama, "yellow"))

#declaramos funcion para limpiar pantalla
def limpiar():
    #ejecutamos el comando clear
    subprocess.run("clear")

#declaramos una funcion para escribir un txt
def escribir(elemento):
    #abrimos un archivo para escribir
    with open("diagrama.py", "a") as f:
        #escribimos en el archivo
        f.write(elemento)
    #mostramos el diagrama
    mostrar()
#creamos una funcion principal
def main():
    #creamos un bucle para solicitar la opcion para trabajar
    while True:
        #limpiamos la pantalla
        limpiar()
        #mostramos el menu principal
        print(colored(menu1, "green"))
        #solicitamos el modo de trabajo
        modo = input("Ingresa el modo de trabajo: ")
        #si el modo es 1
        if modo == "1":
            #limpiamos la pantalla
            limpiar()
            #llamamos a la funcion...
            crear()
        #si el modo es 4
        if modo == "4":
            #limpiamos la pantalla
            limpiar()
            #salimos
            exit("Bye bye :3")
        #y si no...
        else:
            #mostramos un mensaje de error
            print(colored("Modo Desconocido!", "red"))
#creamos una funcion para realizar el ladder
def crear():
    #creamos una variable global para el diagrama
    global diagrama
    #la inicializamos como un string vacio
    diagrama = """"""
    #escribimos los ajustes iniciales
    escribir(ajustes)
    #escribimos el inicio del codigo
    escribir(inicio)
    #ponemos un divisor para las entradas
    diagrama = diagrama + "----------ENTRADAS-----------\n"
    #creamos una variable para los pines de entrada
    entradas = []
    #creamos un bucle para ajustar los pines de entrada
    while True:
        #solicitamos los pines de salida
        pin = input(colored("Seleccione los pines de ENTRADA(Enter para continuar): ", "blue"))
        #si hay datos
        if pin != "":
            #agregamos a los pines de entrada
            entradas.append(pin)
            #escribimos en el diagrama
            diagrama = diagrama + "Entrada en el pin ({})\n".format(pin)
            #escribimos en el codigo
            escribir("    GPIO.setup({}, GPIO.IN)\n".format(pin))
        #y si no
        else:
            #salimos del bucle
            break
    #ponemos un divisor para las entradas
    diagrama = diagrama + "-----------------------------\n"
    #limpiamos la pantalla
    limpiar()
    #ponemos un divisor para las entradas
    diagrama = diagrama + "\n----------SALIDAS----------\n"
    #creamos un bucle para ajustar los pines de salida
    while True:
        #solicitamos los pines de salida
        pin = input(colored("Seleccione los pines de SALIDA(Enter para continuar): ","blue"))
        #si hay datos
        if pin != "":
            #escribimos en el diagrama
            diagrama = diagrama + "Salida en el pin ({})\n".format(pin)
            #escribimos en el codigo
            escribir("    GPIO.setup({}, GPIO.OUT)\n".format(pin))
        #y si no
        else:
            #salimos del bucle
            break
    #ponemos un divisor para las entradas
    diagrama = diagrama + "-----------------------------\n"
    #creamos una variable para saber si se esta editando el diagrama
    edicion = True
    #añadimos el bucle al codigo
    escribir(bucle)
    #añadimos las lecturas de las entradas al codigo
    for pin in entradas:
        #escribimos el pin a leer
        escribir("        contacto{} = GPIO.input({})\n".format(pin, pin))
    #creamos un bucle para que este solicitando los elementos correspondientes
    while edicion:
        #creamos una lista para almacenar los pines
        pines = []
        #creamos un bucle para solicitar el numero de los pines
        while True:
            #mostramos el diagrama
            mostrar()
            #solicitamos los pines a usar
            pin = input(colored("Ingresa:\nPin a usar\n'Enter' para la siguiente linea\n'exit' para terminar\n#: ", "blue"))
            #si el usuario no escribio nada
            if pin == "":
                #ponemos un salto de linea
                diagrama = diagrama + "\n"
                #salimos del bucle
                break
            #si el usuario termino
            elif pin == "exit":
                #creamos una variable para finalizar el codigo
                final = """if __name__ == '__main__':
    try:
        print(colored('''{}''', "yellow"))
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit("Bye bye")\n""".format(diagrama)
                #escribimos el final del codigo
                escribir(final)
                #el modo edicion acabo
                edicion = False
                #salimos del bucle
                break
            #y si no
            else:
                #escribimos en el diagrama el pin
                diagrama = diagrama + "   {}   ".format(pin)
                #mostramos el diagrama
                print(diagrama)
                #agregamos el pin a la lista
                pines.append(pin)
        #creamos una variable para inicio de linea
        linea_inicio = True
        #cremos un bucle para solicitar componentes
        for pin in pines:
            #mostramos el menu
            print(colored(menu2, "green"))
            #solicitamos el componente a usar
            componente = input("Seleccione un componente: ")
            #si la linea esta iniciando...
            if linea_inicio == True:
                #si el usuario usa la opcion 4
                if componente == "exit":
                    #salimos del modo edicion
                    edicion = False
                #y si no...
                else:
                    #si el componente es 1
                    if componente == "1":
                        #escribimos en el diagrama el elemento
                        diagrama = diagrama + "--| |--"
                        #escribimos en el diagrama
                        escribir("        if contacto{}".format(pin))
                        #quitamos el inicio de linea
                        linea_inicio = False
                    #si el componente es 2
                    elif componente == "2":
                        #escribimos en el diagrama el elemento
                        diagrama = diagrama + "--|/|--"
                        #escribimos en el diagrama
                        escribir("        if not contacto{}".format(pin))
                        #quitamos el inicio de linea
                        linea_inicio = False
                    #si el componente es 3
                    elif componente == "3":
                        #escribimos en el diagrama el elemento
                        diagrama = diagrama + "--( )--"
                        #escribimos en el diagrama
                        escribir("""        GPIO.output({}, GPIO.HIGH)\n""".format(pin, pin))
                    #y si no
                    else:
                        #mostramos un error
                        print(colored("Componente Desconocido!!", "red"))
            #y si no..
            else:
                #si el usuario usa la opcion 4
                if componente == "exit":
                    #salimos del modo edicion
                    edicion = False
                    #y si no...
                else:
                    #si el componente es 1
                    if componente == "1":
                        #escribimos en el diagrama el elemento
                        diagrama = diagrama + "--| |--"
                        #escribimos en el diagrama
                        escribir(" and contacto{}".format(pin))
                    #si el componente es 2
                    elif componente == "2":
                        #escribimos en el diagrama el elemento
                        diagrama = diagrama + "--|/|--"
                        #escribimos en el diagrama
                        escribir(" and not contacto{}".format(pin))
                    #si el componente es 3
                    elif componente == "3":
                        #escribimos en el diagrama el elemento
                        diagrama = diagrama + "--( )--\n"
                        #escribimos en el diagrama
                        escribir(""":
            GPIO.output({}, GPIO.HIGH)
        else:
            GPIO.output({}, GPIO.LOW)\n""".format(pin, pin))
                        #agregamos el inicio de linea
                        linea_inicio = True
                    #y si no
                    else:
                        #mostramos un error
                        print(colored("Componente Desconocido!!", "red"))
#creamos un punto de acceso
if __name__ == '__main__':
    #llamamos a la funcion principal
    main()
