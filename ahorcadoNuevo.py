import os
from getpass import getpass
print("***INGRESAR UNA PALABRA PARA EL AHORCADO***")
palabra = getpass("INGRESE AQUÍ: ")
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