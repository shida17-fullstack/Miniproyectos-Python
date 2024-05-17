from unidecode import unidecode  # Importar la función unidecode desde la librería unidecode

def obtener_rating_pelicula(titulo, base_datos):
    # Normalizar y convertir a minúsculas sin acentos
    titulo_normalizado = unidecode(titulo.lower())
    # Buscar el título normalizado en las claves de la base de datos
    for clave in base_datos.keys():
        if unidecode(clave.lower()) == titulo_normalizado:
            return base_datos[clave]
    return "No se encontró la película en la base de datos"

def mostrar_menu(base_datos):
    print("Películas disponibles:")
    for idx, pelicula in enumerate(base_datos.keys(), 1):
        print("{}. {}".format(idx, pelicula.title()))  # Mostrar el título de la película
    print("Ingrese el número de la película (o 'salir' para terminar): ")

# Base de datos de películas con sus ratings
base_datos_peliculas = {
    "Titanic": 7.8,
    "El Padrino": 9.2,
    "Interestelar": 8.6,
    "La La Land": 8.0,
    "Parásitos": 8.6
}

# Mostrar el menú de películas disponibles
mostrar_menu(base_datos_peliculas)

# Ejemplo de uso
while True:
    opcion = input().strip()  # Eliminar espacios en blanco al inicio y al final
    if opcion.lower() == "salir":
        break
    try:
        idx = int(opcion)
        if idx < 1 or idx > len(base_datos_peliculas):
            print("Opción inválida. Introduce un número válido.")
            continue
        titulo_pelicula = list(base_datos_peliculas.keys())[idx - 1]
        rating = obtener_rating_pelicula(titulo_pelicula, base_datos_peliculas)
        print("El rating de la película '{}' es: {}".format(titulo_pelicula, rating))
    except ValueError:
        print("Opción inválida. Introduce un número válido.")

