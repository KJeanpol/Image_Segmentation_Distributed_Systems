import os
from PIL import ImageTk, Image


def to_list(mat):
    res = []
    for i in mat:
        for j in i:
            res += [j]
    return res

def create_file(data, name):
    f_out = open(name, 'w')
    str_data = ''
    for e in data:
        if e <= 9:
            str_data += '00'+str(e)
        elif 10 <= e <= 99:
            str_data += '0'+str(e)
        else:
            str_data += str(e)
    f_out.write(str_data)
    f_out.flush()
    f_out.close()

def binToDecimal():  
    file = open('res.txt', 'r')
    flag=0
    binario=""
    lista=[]
    while 1:       
        # read by character 
        char = file.read(1)           
        if not char:  
            break
        binario=binario+char
        if (flag<7):
            flag=flag+1
        else:
            flag=0
            try:
                elemento=(int(binario,2))
                lista.append(elemento)
                binario=""
            except:
                binario=""
                
    file.close()
    return lista

def ver(n,m,num):
    newdata=binToDecimal()
    newPic = Image.new('L', (m-2,n-2))
    newPic.putdata(newdata)
    if (num==1):    
        newPic.save('test.png')
    else:
        newPic.save('test2.png')
    newPic.close()
    print("CERRE IMAGEN")

def hola(nombre):

    foto = Image.open(nombre)
    image_file = foto.convert('LA') # convert image to black and white
    image_file.save('bw.png')
    foto = foto.convert('L')
    n,m=foto.size
    rows = foto.size[1]
    cols = foto.size[0]
    data = foto.getdata()

    foto.close()
    create_file(data, 'mybin.txt')
    
    sharpen = [[2, 1, 2], [1, 7, 1], [2, 1, 2]]
    create_file(to_list(sharpen), 'kernel.txt')
    create_file([], 'res.txt')
    
    os.system("nasm -f elf64 conv.asm -o conv.o")
    os.system("ld conv.o -o conv")
    os.system("./conv "+str(rows)+" "+str(cols))
    ver(rows,cols,1)

    oversharpen = [[2, 0, 2], [0, 11, 0], [2, 0, 2]]
    create_file(to_list(oversharpen), 'kernel.txt')
    create_file([], 'res.txt')

    os.system("nasm -f elf64 conv.asm -o conv.o")
    os.system("ld conv.o -o conv")
    os.system("./conv "+str(rows)+" "+str(cols))
    ver(rows,cols,2)





    
