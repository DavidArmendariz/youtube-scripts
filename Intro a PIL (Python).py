from PIL import Image
import sys
try:
    img = Image.open("paisaje.jpg")
except:
    print("No se pudo cargar la imagen")
    sys.exit(1)
#img.show()
#Conversión de JPG a PNG
#img.save("paisaje.png","png")
#Rotación de imágenes
#img2 = img.rotate(45)
#img2.show()
#Encontrar ancho y alto de una imagen
#ancho,alto = img.size
#print("Ancho: ",ancho)
#print("Alto: ",alto)7
#Reescalar imágenes y crear thumbnails
#size = (200,200)
#img3 = img.resize(size)
#img4 = img.copy()
#img4.thumbnail(size)
#img3.show()
#img4.show()
#Averiguar los colores de un pixel
#pixels = img.load()
#clr = pixels[10,10]
#print(clr)
