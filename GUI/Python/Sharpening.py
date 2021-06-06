import os
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import numpy as np
import cv2
import PIL
from PIL import ImageTk, Image
import Prueba as Prueba



class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title ("Sharpening & Over-Sharpening")
        self.minsize(1080,720)
       # self.wm_iconbitmap('icon.ico')
        self.var=IntVar()

        self.labelFrame = ttk.LabelFrame(self,text="Open a FILE")
        self.labelFrame.grid(column = 0, row=1, padx=20,pady=20)
        
        self.button()
        self.radioButton()

    def radioEvent(self):
        radSelected= self.radValues.get()
        if (radSelected==1):
            self.createCanvasImage(self.filename)

        elif (radSelected==2):
            self.createCanvasImage('bw.png')
 
        elif (radSelected==3):
            self.createCanvasImage('test.png')

            
        elif (radSelected==4):
            self.createCanvasImage('test2.png')

        else:
            print ("Nada")
        
    def createCanvasImage(self,path):

        self.canvas = Canvas(self, bg="black",height =500,width=500)
        self.canvas.grid (column = 10, row =10)
        
        self.image=Image.open(path)
        m,n=self.image.size
        print("m: "+str(m)+ " r: "+str(n) )
        self.image2=self.image.resize((500,500))

        self.canvas.image= ImageTk.PhotoImage(self.image2)
        self.canvas.create_image(0,0,image=self.canvas.image,anchor='nw')
        
    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File", command = self.fileDialog)
        self.button.grid (column = 1, row =1)

    def radioButton(self):
        self.radValues=IntVar()
        self.r1 = ttk.Radiobutton(self.labelFrame, text = "Normal", variable=self.radValues, value=1, command = self.radioEvent)
        self.r1.grid (column = 4, row =1)
        
        self.r1 = ttk.Radiobutton(self.labelFrame, text = "Black and White", variable=self.radValues, value=2, command = self.radioEvent)
        self.r1.grid (column = 4, row =5)
        
        self.r2 = ttk.Radiobutton(self.labelFrame, text = "Sharpening", variable=self.radValues,value=3, command = self.radioEvent)
        self.r2.grid (column = 4, row =10)
        
        self.r3 = ttk.Radiobutton(self.labelFrame, text = "Over-Sharpening", variable=self.radValues,value=4, command = self.radioEvent)
        self.r3.grid (column = 4, row =15)
        
        
    def fileDialog(self):
        self.filename = filedialog.askopenfilename (initialdir = "/", title = "Select a File",filetypes=(('png','*.png'),
                                                ('bmp','*.bmp'),('jpeg','*.jpeg'),('Todos os arquivos','*.*')))

        Prueba.hola(self.filename)


if __name__ == '__main__':
    root = Root()
    root.mainloop()
