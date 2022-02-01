# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:02:03 2022

@author: AndreaCosioFernández
"""
import random

print("Bienvenido al piedra, papel, tijera online")
print("---------------------------------------------")
print("|                 ♥ MENÚ ♥                  |")                
print("---------------------------------------------")
print("| 1.Elegir nicks del jugador                |")
print("| 2.Partida rapida                          |")
print("| 3.Partida completa                        |")
print("| 4.Salir                                   |")
print("| 5.Creditos                                |")
print("---------------------------------------------")

piedra=1
papel=2
tijera=3
lagarto=4
spock=5

valormenu=int(input("Seleccione una opción:"))

if valormenu==1:
    nick=int(input("Seleccione nick:"))
    
elif valormenu==2:
    eleccion=int(input("Teniendo en cuenta que el 1=piedra, el 2=papel y el 3=tijera, seleccione un número del 1 al 3:"))
    if eleccion <=3 or eleccion >=1:
        print(f"Has elegido {eleccion}")
        maquina=random.randrange(3)
        print(f"{nick} ha sacado {eleccion} y la maquina ha sacado{maquina}")
        if eleccion==1:
            if maquina==1:
                print(f"La máquina y tu {nick} habeis empatado") 
            elif maquina==2:
                print("Ha ganado la Maquina :(")
            elif maquina==3:
                print("Has ganado tú :)")
                    
        if eleccion==2:
            if maquina==1:
                print("Has ganado tú :)") 
            elif maquina==2:
                print(f"La máquina y tu {nick} habeis empatado")
            elif maquina==3:
                print("Ha ganado la Maquina :(")
                    
        elif eleccion==3:
            if maquina==1:
                print("Ha ganado la Maquina :(") 
            elif maquina==2:
                print("Has ganado tú :)")
            elif maquina==3:
                print(f"La máquina y tu {nick} habeis empatado")

elif valormenu==3:
    eleccionp=int(input("Teniendo en cuenta que el 1=piedra, el 2=papel, el 3=tijera, el 4=lagarto y el 5=spock seleccione un número del 1 al 5:"))
    if eleccionp <=5 or eleccion >=1:
        print(f"Has elegido {eleccionp}")
        maquinap=random.randrange(5)
        print(f"{nick} ha sacado {eleccion} y la maquina ha sacado{maquina}")

    if eleccion==1:#piedra
        if maquina==1:
            print(f"La máquina y tu {nick} habeis empatado") 
        elif maquina==2:
            print("Ha ganado la Maquina :(")
        elif maquina==3:
            print("Has ganado tú :)")
        elif maquina==4:
            print("Has ganado tú :)")
        elif maquina==5:
            print("Ha ganado la Maquina :(")
                
    if eleccion==2:#papel
        if maquina==1:
            print("Has ganado tú :)") 
        elif maquina==2:
            print(f"La máquina y tu {nick} habeis empatado")
        elif maquina==3:
            print("Ha ganado la Maquina :(")
        elif maquina==4:
            print("Ha ganado la Maquina :(")
        elif maquina==5:
            print("Has ganado tú :)")
                
    elif eleccion==3:#tijera
        if maquina==1:
            print("Ha ganado la Maquina :(") 
        elif maquina==2:
            print("Has ganado tú :)")
        elif maquina==3:
             print(f"La máquina y tu {nick} habeis empatado")   
        elif maquina==4:
            print("Has ganado tú :)")
        elif maquina==5:
            print("Ha ganado la Maquina :(")
    
    elif eleccion==4:#lagarto
        if maquina==1:
            print("Ha ganado la Maquina :(") 
        elif maquina==2:
            print("Has ganado tú :)")
        elif maquina==3:
            print("Ha ganado la Maquina :(")    
        elif maquina==4:
            print(f"La máquina y tu {nick} habeis empatado")
        elif maquina==5:
            print("Has ganado tú :)")
            
    elif eleccion==5:#spock
        if maquina==1:
            print("Has ganado tú :)")
        elif maquina==2:
            print("Ha ganado la Maquina :(")
        elif maquina==3:
            print("Has ganado tú :)")
        elif maquina==4:
            print("Ha ganado la Maquina :(")
        elif maquina==5:
            print(f"La máquina y tu {nick} habeis empatado")
    
    

    