#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#menu principal
menu = """
1) -| |-
2) -|/|-
3) -( )-
4) -(fin)-
"""

#creamos una funcion principal
def main():
    #cremos un bucle para solicitar componentes
    while True:
        #mostramos el menu
        print(menu)
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
                pass
            #si el componente es 2
            elif componente == "2":
                pass
            #si el componente es 3
            elif componente == "3":
                pass

#creamos un punto de acceso
if __name__ == '__main__':
    #llamamos a la funcion principal
    main()
