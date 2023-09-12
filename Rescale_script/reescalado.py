import os
from PIL import Image


directorio_entrada = 'original'
directorio_salida = 'thumbnails'

# Lado en pixeles del largo deseado
lado_largo_deseado = 640


if not os.path.exists(directorio_salida): # Asegurarse de que el directorio de salida exista
    os.makedirs(directorio_salida)

reescalado_realizado = False    # Comprueba si se ha realizado el reescalado en al menos una imagen.
cantidad_reescalada = 0         # Variable para rastrear la cantidad de imágenes reescaladas

try:
    archivos_entrada = os.listdir(directorio_entrada)
    archivos_salida = os.listdir(directorio_salida)

    for archivo in archivos_entrada:
        if archivo.lower().endswith(('.jpg', '.jpeg', '.png')) and archivo not in archivos_salida:
            imagen = Image.open(os.path.join(directorio_entrada, archivo))

            # Calcular el nuevo tamaño manteniendo la proporción
            ancho, alto = imagen.size
            if ancho >= alto:
                proporcion = lado_largo_deseado / ancho
                nuevo_ancho = lado_largo_deseado
                nuevo_alto = int(alto * proporcion)
            else:
                proporcion = lado_largo_deseado / alto
                nuevo_alto = lado_largo_deseado
                nuevo_ancho = int(ancho * proporcion)


            imagen_reescalada = imagen.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS) # Reescalar la imagen
            imagen_reescalada.save(os.path.join(directorio_salida, archivo)) # Guardar la imagen en el directorio de salida con el mismo nombre

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
