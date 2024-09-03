import random


def adivinanza_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("Bienvenido al juego de adivinanza de un número")
    print("Debes adivinar un número entre el 1 al 100 ¡Intenta adivinarlo!")

    while not adivinado:
        adivinanza = input("Introduzca un número del 1 al 100: ")

        # Verificar que la entrada sea un número
        if adivinanza.isdigit():
            adivinanza = int(
                adivinanza
            )  # Estamos pasando de texto a entero | pasando de tipo string a boolean
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(
                    f"¡Felicidades has ganado!, el número {adivinanza} es el número secreto y lo has logrado en {intentos} intentos."
                )
        else:
            print("Por favor ingresa un número válido entre el 1 al 100")

adivinanza_numero()