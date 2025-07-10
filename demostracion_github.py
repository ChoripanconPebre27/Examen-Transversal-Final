mundo = "Hola Mundo!"
siete = "Me voy a sacar un 7"

while True:
    elije = input("Elije uno de los mensajes: ")
    try:
        elije = int(elije)
    except:
        print("ERROR: El valor no es un entero.")
        continue
    if elije == 1:
        print(mundo)
        print("Felicidades! Pudiste avanzar correctamente.")
        break
    elif elije == 2:
        print(siete)
        print("Felicidades! Pudiste avanzar correctamente.")
        break
    else:
        print("No coincide.")
        print("Intentalo de nuevo.")