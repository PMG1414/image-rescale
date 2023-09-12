import os
from PIL import Image


directorio_entrada = 'original'
directorio_salida = 'thumbnails'

# Porcentaje de reescalado (50 es a la mitad, 200 es el doble, etc)
porcentaje_reescalado = 50


if not os.path.exists(directorio_salida): # Asegurarse de que el directorio de salida exista
    os.makedirs(directorio_salida)

reescalado_realizado = False    # Comprueba si se ha realizado el reescalado en al menos una imagen.
cantidad_reescalada = 0         # Variable para rastrear la cantidad de imágenes reescaladas

try:
    archivos = os.listdir(directorio_entrada) # Lista todos los archivos en el directorio de entrada

    for archivo in archivos:
        if archivo.lower().endswith(('.jpg', '.jpeg', '.png')):
            imagen = Image.open(os.path.join(directorio_entrada, archivo))

            # Calcular las nuevas dimensiones manteniendo la proporción
            ancho, alto = imagen.size
            nuevo_ancho = int(ancho * (porcentaje_reescalado / 100))
            nuevo_alto = int(alto * (porcentaje_reescalado / 100))

            imagen_reescalada = imagen.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS) # Reescalar la imagen
            imagen_reescalada.save(os.path.join(directorio_salida, archivo) )# Guardar la imagen en el directorio de salida con el mismo nombre

            reescalado_realizado = True
            cantidad_reescalada += 1

    if reescalado_realizado:
        print(f"Reescalado completado. Se reescalaron {cantidad_reescalada} imágenes.")
    else:
        print("Alerta: No se reescaló ninguna imagen porque todas coinciden en la carpeta de thumbnails.")

except FileNotFoundError:
    print("Error: El directorio de entrada no existe o no contiene archivos de imagen.")
except Exception as e:
    print(str(e))