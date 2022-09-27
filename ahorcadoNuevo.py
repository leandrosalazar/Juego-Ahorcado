import os
from getpass import getpass
print()
print("***INGRESAR UNA PALABRA PARA EL AHORCADO***")
print()
print("***LA PALABRA SERÁ INVISIBLE PARA QUE LA OTRA PERSONA NO LA VEA***")
print()
print("***PUEDE OPTAR POR VERLA AHORA PARA CORREGIRLA, O SEGUIR CON LA MISMA PALABRA***")
print()
palabra = getpass("INGRESE AQUÍ: ")
opcion = input("¿Queres ver la palabra que escribiste? S/N: ")
if opcion.upper() == "S":
    segundaOpcion = input(f"La palabra que escribiste fue {palabra}. ¿Quieres cambiarla? S/N: ")
    if segundaOpcion.upper() == "S":
        palabra = getpass("Escribí de nuevo tu palabra u otra que quieras: ")
    elif segundaOpcion.upper() == "N":
        print("***GENIAL, COMENCEMOS***")
    else:
        print("Me queres romper el sistema papu? Nos vemos -.-")
        quit()
elif opcion.upper() == "N":
    print("***GENIAL, COMENCEMOS***")
else:
    print("Me queres romper el sistema papu? Nos vemos -.-")
    quit()
palabralista = list(palabra)
ahorca = ["         !=======(A)",
         "                  (H)",
         "                  (O)",
         "                  (R)",
         "                  (C)",
         "                  (A)",
         "                  (D)",
         "     _____________(O)"]             
ahorcado = ["      |===========(A)",
            "      |___◯       (H)",
            "         /|\      (O)",
            "        / | \     (R)",
            "         / \      (C)",
            "        /   \     (A)",
            "       _\    \_   (D)",
            "     _____________(O)"]
letrasUsadas = []
errores = 1
listavacia = []
for x in range(len(palabralista)):
    listavacia.append("_")
print(listavacia)
while True:
    os.system("cls")
    print("****** A JUGAR *******")
    for i in range(errores):
        print(ahorcado[i])
    for i in range(len(ahorca) - errores):
        print(ahorca[i+errores])
    print("")
    print("     ", end=" ")
    for i in listavacia:
        print(i, end=" ")
    print("")
    print("")
    if listavacia == palabralista:
        print("**FELICIDADES, GANASTE EL JUEGO DEL AHORCADO**")
        break
    if errores > 6:
        print("La palabra era:  " ,"".join(palabralista))
        print("****** PERDISTE ******")
        break    
    while True:
        letra = input("Ingrese una letra para adivinar el ahorcado: ")
        if len(letra) != 1:
            print("Ingresar una sola letra")
        elif letra not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("Ingrese una letra válida")
        elif letra in letrasUsadas:
            print("Esa letra ya la ingresaste")
        else:
            letrasUsadas.append(letra)
            break   
    if letra in palabralista:
        for index, value in enumerate(palabralista):
            if value == letra:
                listavacia[index] = letra
    else:
        errores += 1       