#Librerias
import numpy as np
import cv2
import os
from os import listdir
from Tkinter import Tk
from Tkinter import *
from tkFileDialog import askdirectory as directory
import math

address_folder_img=None
address_folder_txt=None
img_read=False
txt_read=False

def folder_img():
	global address_folder_img,img_read,txt_read
	Tk().withdraw()
	address_folder_img = directory()
	print(address_folder_img)
	#for file_img in listdir(address_folder_img):
	#	print(file_img)
	img_read=True
	if img_read and txt_read:
		read_file()
	
def folder_txt():
	global address_folder_txt,img_read,txt_read
	Tk().withdraw()
	address_folder_txt = directory()
	print(address_folder_txt)
	#for file_txt in listdir(address_folder_txt):
	#	print(file_txt)
	txt_read = True
	if img_read and txt_read:
		read_file()

def read_file():
	global address_folder_img,address_folder_txt
	for name_file_img in listdir(address_folder_img):
		print ("Escribiendo imagen: "+name_file_img)
		file_name = name_file_img.split(".")[0]
		folder=r'Conjunto_Baches/'+ file_name
		if not os.path.exists(folder): os.makedirs(folder)
		file_txt = open(address_folder_txt+"/bache_"+file_name+".txt","r")
		image=cv2.imread(address_folder_img+"/"+file_name+".jpeg")
		index=0
		for puntos in file_txt:
			x_,y_,radius_= puntos.split(",")
			x,y,radius = int(x_),int(y_),int(radius_)
			cv2.imwrite(folder+'/bache_'+file_name+'_'+str(index)+'.jpg', write_img(x,y,radius,image))
			index+=1

def write_img(x,y,radius,image):
	x_init,x_end,y_init,y_end=0,image.shape[1],0,image.shape[0]
	if x - radius >= 0: 
		x_init = x - radius
	if x + radius <= image.shape[1]:
		x_end = x + radius
	if y - radius >= 0: 
		y_init = y - radius
	if y + radius <= image.shape[0]:
		y_end = y + radius
	return image[y_init:y_end,x_init:x_end]

#main
if __name__ == '__main__':
	root=Tk()
	root.geometry('300x80')
	root.resizable(0,0)
	root.title('Deteccion de baches')
	button = Button(root,text="Seleccione la carpeta de archivos txt",command=folder_txt)
	button.pack()
	button2 = Button(root,text="Seleccione la carpeta de imagenes",command=folder_img)
	button2.pack()
	exit = Button(root, text='Presiona este [Button para Salir]', command=root.quit)
	exit.pack()
	root.mainloop()
	
