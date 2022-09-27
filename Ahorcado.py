from multiprocessing.sharedctypes import Value
print()
print("¡VAMOS A JUGAR AL AHORCADO!")
palabraAdivinar = input("Ingrese una palabra para que sea adivinada: ")
palabralista = list(palabraAdivinar)
listaVacia = []
for x in palabralista:
    if x in palabralista:
        listaVacia.append("_")
contador = 0
while contador < 10:
    letra = input("Ingrese una letra: ")
    if len(letra) == len(palabraAdivinar):
        if letra == palabraAdivinar:
            print("¡Felicidades, acertaste! Te quedaron",10 - contador," intentos restantes")
            quit()
    if len(letra) == 1:          
        for index, value in enumerate(palabralista):   
            if letra in palabralista:
                if value == letra:
                    listaVacia[index] = letra
                    print(listaVacia)
                    if listaVacia == palabralista:
                        print("¡Felicidades, acertaste! Te quedaron",10 - contador," intentos restantes")
                        quit()
    else:
        print("NO SE PUEDE")
        quit()
    if letra not in palabraAdivinar:
        contador += 1
        print(f"La letra '{letra}' no está en la palabra. Tenes {contador} intentos de 10")
    if contador == 10:
        print("XD bye")
print()