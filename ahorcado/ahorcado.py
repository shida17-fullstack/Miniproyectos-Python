import random

# Lista de palabras para el juego
palabras = ["python", "programacion", "computadora", "inteligencia", "artificial", "algoritmo", "datos", "informatica"]

def obtener_palabra_al_azar():
    # Seleccionar una palabra al azar de la lista de palabras
    return random.choice(palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    # Mostrar la palabra secreta con letras adivinadas y espacios para letras no adivinadas
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero

def jugar_ahorcado():
    print("¡Bienvenido al Juego del Ahorcado!")
    palabra_secreta = obtener_palabra_al_azar()
    letras_adivinadas = []
    intentos_restantes = 6  # Número de intentos permitidos

    while True:
        print("\n" + mostrar_tablero(palabra_secreta, letras_adivinadas))
        if "_" not in mostrar_tablero(palabra_secreta, letras_adivinadas):
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break
        if intentos_restantes == 0:
            print("¡Oh no! ¡Has agotado todos tus intentos! La palabra era: " + palabra_secreta)
            break

        letra = input("Ingresa una letra: ").lower()  # Convertir a minúsculas
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una sola letra.")
            continue
        if letra in letras_adivinadas:
            print("Ya has ingresado esta letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)
        if letra not in palabra_secreta:
            intentos_restantes -= 1
            print("¡Letra incorrecta! Te quedan {} intentos.".format(intentos_restantes))

# Iniciar el juego
jugar_ahorcado()
