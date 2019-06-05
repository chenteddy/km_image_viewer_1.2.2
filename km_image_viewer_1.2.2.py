import io  
import tkinter as tk
from os import listdir
from os.path import isfile, isdir, join
from PIL import Image, ImageTk
from tkinter import filedialog as fd
homepage=tk.Tk()
homepage.title('KM_image_viewer_1.2.1.released')
homepage.geometry("600x600")
iconimg = ImageTk.PhotoImage(file='icon.ico')
homepage.tk.call('wm', 'iconphoto', homepage._w, iconimg)
#homepage.resizable(0,0) #視窗左上座標 0,0為鎖定縮放
#元件變數=元件名稱(容器物件變數, [元件選項])  標籤文字 (text), 大小(size), 邊框 (border), 前景顏色 (foreground), 或背景顏色 (background)
label=tk.Label(homepage, text="按下OK切換下一張圖片")   #建立標籤物件
filename=tk.Label(homepage, text="",width='70')
icount=0
imageSource_list=[]
imageSource=[]
loadfolder_=[]
musicimage=tk.Label(homepage,height='500',width='500')
def clickLoad():
     global loadfolder_
     loadfolder=fd.askdirectory()
     loadfolder_=loadfolder[loadfolder.find('/'):len(loadfolder)]
     viewimage()
     return loadfolder_

#####圖片顯示#####
def resize(w, h, w_box, h_box, pil_image):  
     f1 = 1.0*w_box/w
     f2 = 1.0*h_box/h  
     factor = min([f1, f2])  
     width = int(w*factor)  
     height = int(h*factor)  
     return pil_image.resize((width, height), Image.ANTIALIAS)
def viewimage():
     imagefolder= loadfolder_
     imagefolder_a=listdir(imagefolder)
     global imageSource_list
     global imageSource
     for i in imagefolder_a:
          imageSource_list.append(join(imagefolder,i))
          joinimage=Image.open(join(imagefolder,i))
          w_box , h_box= 500 , 500
          w, h = joinimage.size
          image_resized = resize(w, h, w_box, h_box, joinimage)
          imageSource.append(ImageTk.PhotoImage(image_resized))
     image1 = imageSource[icount]
     musicimage=tk.Label(homepage,image=image1)
     musicimage.grid(column=1,row=2)
     filename.grid(column=1,row=1)
     return imageSource_list,imageSource
def changeImage(x):
     global icount
     global musicimage
     global imageSource_list
     global imageSource
     if x =='N':
          icount +=1
     else:
          icount -=1
          if icount < 0:
               icount=len(imageSource_list)-1
     if icount >= len(imageSource_list):
          icount=0
     image1 = imageSource[icount]
     image0 = ImageTk.PhotoImage(file='none.png')
     musicimage=tk.Label(homepage,image=image0,height='500',width='500')
     musicimage.grid(column=1,row=2)
     musicimage=tk.Label(homepage,image=image1)
     musicimage.grid(column=1,row=2)
#####圖片顯示#####

#####按鍵控制#####
count=0     
def clickNext():
     changeImage('N')
     global count
     global icount
     count=count + 1
     label.configure(text="此為第" + str(icount+1) + "張圖片")
     filename.configure(text="檔案位置:" +imageSource_list[icount])
     print(imageSource_list[icount])
def clickLast():
     changeImage('L')
     global count
     global icount
     count=count + 1
     label.configure(text="此為第" + str(icount+1) + "張圖片")
     filename.configure(text="檔案位置:" +imageSource_list[icount])
buttonNext=tk.Button(homepage, text="下一張", command=clickNext)
buttonLast=tk.Button(homepage, text="上一張", command=clickLast)
buttonLoad=tk.Button(homepage, text='Load',command=clickLoad)
#####按鍵控制#####

#####將元件放入容器#####
#label.pack()       
#buttonNext.pack()
#buttonLast.pack()
#musicimage.pack()
label.grid(column=1,row=0)
buttonLoad.grid(column=0,row=0)
#filename.grid(column=1,row=1)
buttonNext.grid(column=2,row=1)
buttonLast.grid(column=0,row=1)
#musicimage.grid(column=1,row=2)
#####將元件放入容器#####

#####執行#####
homepage.mainloop()
#####執行#####
# -*- coding:utf-8 -*-

