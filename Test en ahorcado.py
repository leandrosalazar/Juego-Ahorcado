clave=[]
espacio=[]
datos=input("Ingrese la palabra a adivinar: ")
#creo una lista llamada "clave" con cada letra y una lista con espacios, por cada letra
for i in datos:
    clave.append(i)
    espacio.append("_")
print(f"Adivinemos la palabra! Su largo es de {len(clave)} casilleros\n")
print(espacio)
adivina=None #creamos una variabla "adivina" para dar valor al proximo while
intentos=7
while datos != adivina and intentos !=0: #este while sirve para realizar el juego, hasta que la palabra se adivine o se acaben los intentos
    letra = input("Elija una letra: ") #pedimos una letra, y usamos este for para recorrer la lista clave y ver si esta la letra.
    contador = 0
    for x in range(len(clave)):
        if letra == clave[x]: #si encontramos una coincidencia, pegamos esa letra en la misma posicion de la lista espacio
            espacio[x]=letra.upper()
            contador = contador+1
    if contador ==0:
        intentos = intentos-1
        print(f'No acertaste la letra! te quedan {intentos} intentos')
    if intentos == 0:
        print(f'GAME OVER! La palabra era {datos.upper()}')
        break
    print(espacio)
    opcion = "" #con la variable opcion, le damos un valor al while.
    while opcion != "n": #en este ciclo, preguntamos si quiere arriesgar una palabra. Si la acierta termina, sino sigue el juego
        opcion= input("¿Arriesgas una palabra? S/N: ")
        if opcion == "s":
            adivina=input("Introduzca la palabra: ")
            if adivina==datos:
                print(f"Acertaste!! La palabra era {datos.upper()}\nGracias por jugar!!")
                opcion="n"
            else:
                intentos=intentos-1
                print(f"No es la palabra correcta! Te quedan {intentos} intentos \n")
                break
        elif opcion == "n":
            print("Continuemos jugando!\n")
        else:
            print("Eligio una opcion no valida\n")