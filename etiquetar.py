#Librerias
import numpy as np
import cv2
import os
from Tkinter import Tk
from Tkinter import *
#from Tkinter.filedialog import askopenfilename
from tkFileDialog import askopenfilename
import math

file_name=""
radius=True
xi,yi=0,0

#Evento
def x_or_y(event,x,y,flags,param):
    global file_name,radius,xi,yi
    if event == cv2.EVENT_LBUTTONDOWN:
    	if radius:
    		xi,yi=x,y
    		radius=False
    	else:
    		folder=r'Baches_Txt'
    		if not os.path.exists(folder): os.makedirs(folder)
    		d=int(math.sqrt((x-xi)**2+(y-yi)**2))
    		f = open ("Baches_Txt/bache_"+file_name+".txt","a")
    		f.write(str(xi)+","+str(yi)+","+str(d)+"\n")
    		f.close()
    		cv2.circle(param, (xi,yi), d, (0,0,255), 1, cv2.LINE_AA)
    		xi,yi=0,0
    		radius=True
	
#funcion
def start_init():	
	global file_name
	Tk().withdraw()
	#file_address = askopenfilename(initialdir = "/home/cano/Vuelo",title = "Select file",filetypes=[("Pictures","*.png")])
	file_address = askopenfilename(title = "Select file",filetypes=[("Pictures","*.jpeg")])
	file_name=file_address.split("/")[-1].split(".")[0]
	img = cv2.imread(file_address)
	cv2.namedWindow(file_address)
	cv2.setMouseCallback(file_address,x_or_y,img)

	while(1):
		cv2.imshow(file_address,img)
		key = cv2.waitKey(20) & 0xFF;
		if key == 27:
			break
	folder=r'Baches_Img'
	if not os.path.exists(folder): os.makedirs(folder)
	cv2.imwrite('Baches_Img/bache_'+file_name+'.jpg', img)
	cv2.destroyAllWindows()
	radius=True
	file_name=""
	xi,yi=0,0

#main
if __name__ == '__main__':
	root=Tk()
	root.geometry('300x80')
	root.resizable(0,0)
	root.title('Etiquetado de baches')
	button = Button(root,text="Buscar Imagen",command=start_init)
	button.pack()
	exit = Button(root, text='Presiona este [Button para Salir]', command=root.quit)
	exit.pack()
	root.mainloop()
	
