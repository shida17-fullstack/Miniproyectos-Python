UNIDADES = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
DECENAS = ['diez', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
CENTENAS = ['cien', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']

def convertir_unidades(numero):
    return UNIDADES[numero]

def convertir_decenas(numero):
    if numero < 10:
        return convertir_unidades(numero)
    elif numero == 10:
        return DECENAS[0]
    elif numero < 20:
        if numero == 15:
            return 'quince'
        else:
            return 'dieci' + convertir_unidades(numero - 10)
    else:
        decena = numero // 10
        unidad = numero % 10
        if unidad == 0:
            return DECENAS[decena - 1]
        else:
            return DECENAS[decena - 1] + ' y ' + convertir_unidades(unidad)

def convertir_centenas(numero):
    if numero < 100:
        return convertir_decenas(numero)
    elif numero == 100:
        return CENTENAS[0]
    else:
        centena = numero // 100
        resto = numero % 100
        if resto == 0:
            return CENTENAS[centena - 1]
        else:
            return CENTENAS[centena - 1] + ' ' + convertir_decenas(resto)

def convertir_numero_a_palabras(numero):
    if numero < 1000:
        return convertir_centenas(numero)
    else:
        return 'Número fuera de rango'

# Solicitar al usuario que ingrese un número aleatorio
numero = int(input("Ingresa un número entre 0 y 999: "))
print(convertir_numero_a_palabras(numero))
