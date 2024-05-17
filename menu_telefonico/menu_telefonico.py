import re

def mostrar_menu():
    print("Bienvenido al menú telefónico:")
    print("1. Consultar saldo")
    print("2. Recargar saldo")
    print("3. Transferir saldo")
    print("4. Salir")

def consultar_saldo(saldo):
    print("Tu saldo actual es ${}".format(saldo))

def recargar_saldo(saldo):
    print("Por favor, ingresa el monto a recargar:")
    monto = float(input())
    saldo += monto
    print("Recargaste ${} exitosamente.".format(monto))
    return saldo

def transferir_saldo(saldo):
    intentos = 0
    while intentos < 3:
        print("Por favor, ingresa el número de teléfono al que deseas transferir:")
        numero = input()
        # Validar el formato del número de teléfono utilizando una expresión regular
        if not re.match(r"^15\d{8}$", numero):
            print("El número de teléfono debe comenzar con '15' seguido de 8 dígitos. Inténtalo de nuevo.")
            intentos += 1
        else:
            print("Por favor, ingresa el monto a transferir:")
            monto = float(input())
            saldo_despues_transferencia = saldo - monto
            if saldo_despues_transferencia < 0:
                print("Fondos insuficientes. No puedes transferir más dinero del que tienes.")
            else:
                saldo -= monto
                print("Has transferido ${} al número {} exitosamente.".format(monto, numero))
            return saldo
    else:
        print("Has excedido el límite de intentos. Volviendo al menú.")
        return saldo

def main():
    saldo = 100

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            consultar_saldo(saldo)
        elif opcion == "2":
            saldo = recargar_saldo(saldo)
        elif opcion == "3":
            saldo = transferir_saldo(saldo)
        elif opcion == "4":
            print("Gracias por usar nuestro servicio. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
