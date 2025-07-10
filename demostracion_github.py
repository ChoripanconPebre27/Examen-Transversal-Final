mundo = "Hola Mundo!"
siete = "Me voy a sacar un 7"

elije = input("Elije uno de los mensajes: ")

try:
    elije = int(elije)
except:
    print("ERROR: El valor no es un entero.")

if elije == "1":
    print(mundo)
elif elije == "2":
    print(siete)
else:
    print("No coincide.")