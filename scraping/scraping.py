import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5500/Miniproyectos-JavaScript/scroll_infinito/index.html"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraer el título de la página
    title = soup.title.text
    print("Título de la página:", title)
    
    # Encontrar todos los enlaces en la página
    links = soup.find_all('a')
    print("\nEnlaces encontrados:")
    for link in links:
        print(link.get('href'))
    
    # Encontrar todas las imágenes en la página
    images = soup.find_all('img')
    print("\nImágenes encontradas:")
    for image in images:
        print(image.get('src'))
    
    # Extraer todo el texto de la página
    text = soup.get_text()
    print("\nTexto de la página:")
    print(text)
else:
    print("Error al realizar la solicitud:", response.status_code)
