import os
from PIL import ImageTk, Image

def main(nombre,algoritmo,n1,n2,n3,n4):

    foto = Image.open(nombre)
    image_file = foto.convert('LA') # convert image to black and white
    image_file.save('bw.png')
    foto = foto.convert('L')
    n,m=foto.size
    rows = foto.size[1]
    cols = foto.size[0]
    data = foto.getdata()
    foto.close()
    
    os.system("mpiexec -n 1 -hostfile config ./prueba osito")







    
