import os
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import numpy as np
import cv2
import PIL
from PIL import ImageTk, Image
import Facade as Facade



class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title ("Sharpening & Over-Sharpening")
        self.minsize(1080,720)
       # self.wm_iconbitmap('icon.ico')
        self.var=IntVar()
        self.var2=IntVar()

        self.labelFrame = ttk.LabelFrame(self,text="Ver Imagen")
        self.labelFrame.grid(column = 0, row=300, padx=20,pady=20)

        self.labelFrame1 = ttk.LabelFrame(self,text="Control Nodos")
        self.labelFrame1.grid(column = 0, row=1, padx=20,pady=20)    

        self.labelFrame2 = ttk.LabelFrame(self,text="Algoritmos")
        self.labelFrame2.grid(column = 0, row=200, padx=20,pady=20)    
        

        self.labelFrame3 = ttk.LabelFrame(self,text="Acciones")
        self.labelFrame3.grid(column = 0, row=400, padx=20,pady=20)    

        self.VerImagenes()
        self.Algoritmos()
        self.button()
        self.ControlNodos()


    def VerImagenes(self):
        self.radValues=IntVar()
        
        self.r3 = ttk.Radiobutton(self.labelFrame, text = "Imagen normal", variable=self.radValues,value=1, command = self.radioEvent)
        self.r3.grid (column = 4, row =10)
        
        self.r4 = ttk.Radiobutton(self.labelFrame, text = "Imagen procesada", variable=self.radValues,value=2, command = self.radioEvent)
        self.r4.grid (column = 4, row =15)

    def Algoritmos(self):
        self.radValues2=IntVar()
        self.r1 = ttk.Radiobutton(self.labelFrame2, text = "Algoritmo 1", variable=self.radValues2, value=1)
        self.r1.grid (column = 4, row =1)
        
        self.r2= ttk.Radiobutton(self.labelFrame2, text = "Algoritmo 2", variable=self.radValues2, value=2)
        self.r2.grid (column = 4, row =5)

        
    def button(self):
        self.button = ttk.Button(self.labelFrame3, text = "Iniciar", command = self.fileDialog)
        self.button.grid (column = 1, row =1)

        self.button = ttk.Button(self.labelFrame3, text = "Estadisticas", command = self.Ejemplo)
        self.button.grid (column = 5, row =1)

        
    def ControlNodos(self):
        
        self.lbl1 = ttk.Label(self.labelFrame1, text = "Nodo 1")
        self.lbl1.grid (column = 1, row =1)
        self.nodo1 = ttk.Entry(self.labelFrame1)
        self.nodo1.grid (column = 20, row =1)

        self.lbl2 = ttk.Label(self.labelFrame1, text = "Nodo 2")
        self.lbl2.grid (column = 1, row =10)
        self.nodo2 = ttk.Entry(self.labelFrame1)
        self.nodo2.grid (column = 20, row =10)

        self.lbl3 = ttk.Label(self.labelFrame1, text = "Nodo 3")
        self.lbl3.grid (column = 1, row =20)
        self.nodo3 = ttk.Entry(self.labelFrame1)
        self.nodo3.grid (column = 20, row =20)

        self.lbl4 = ttk.Label(self.labelFrame1, text = "Nodo 4")
        self.lbl4.grid (column = 1, row =30)
        self.nodo4 = ttk.Entry(self.labelFrame1)
        self.nodo4.grid (column = 20, row =30)



    def radioEvent(self):
        radSelected= self.radValues.get()
        if (radSelected==1):
            self.createCanvasImage(self.filename)

        elif (radSelected==2):
            self.createCanvasImage('bw.png')

        else:
            print ("Nada")
        
    def createCanvasImage(self,path):

        self.canvas = Canvas(self, bg="black",height =500,width=500)
        self.canvas.grid (column = 100, row =10)
        
        self.image=Image.open(path)
        m,n=self.image.size
        print("m: "+str(m)+ " r: "+str(n) )
        self.image2=self.image.resize((500,500))

        self.canvas.image= ImageTk.PhotoImage(self.image2)
        self.canvas.create_image(0,0,image=self.canvas.image,anchor='nw')


    def Ejemplo(self):
        radSelected= self.radValues.get()
        radSelected2= self.radValues2.get()
        
        print(radSelected)
        print(radSelected2)
        print(self.nodo4.get())

    def fileDialog(self):
        self.filename = filedialog.askopenfilename (initialdir = "/", title = "Select a File",filetypes=(('png','*.png'),
                                                ('bmp','*.bmp'),('jpeg','*.jpeg'),('Todos os arquivos','*.*')))


        algoritmo= self.radValues2.get()
        n1 = self.nodo1.get()
        n2 = self.nodo2.get()
        n3 = self.nodo3.get()
        n4 = self.nodo4.get()
        
        Facade.main(self.filename,algoritmo,n1,n2,n3,n4)


if __name__ == '__main__':
    root = Root()
    root.mainloop()
