from distutils.cmd import Command
from fileinput import close
from tkinter import*
import tkinter as tk
from PIL import Image, ImageTk
from email.mime import image
from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk
# Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io



root = Tk()
root.minsize(height=500, width=600)


def pest_counter(image):
  #image = cv2.imread('/content/indexw.jpg')
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  #plt.imshow(gray, cmap='gray')
  blur = cv2.GaussianBlur(gray, (11, 11), 0)
  #plt.imshow(blur, cmap='gray')
  canny = cv2.Canny(blur, 30, 150, 3)
  #plt.imshow(canny, cmap='gray')
  dilated = cv2.dilate(canny, (1, 1), iterations=0)
  #plt.imshow(dilated, cmap='gray')

  (cnt, hierarchy) = cv2.findContours(
    dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

  #plt.imshow(rgb)

  #print("pests in the image : ", len(cnt))
  return len(cnt)


def destroy_third():
    third_frame.frm.destroy()
    third_frame.label3.destroy()
    third_frame.button4.destroy()
    third_frame.lbl2.destroy()
    third_frame.button5.destroy()
    second_frame()
    



def destroy_second():
    second_frame.frm.destroy()
    second_frame.label2.destroy()
    second_frame.button2.destroy()
    second_frame.lbl.destroy()
    show_image.button3.destroy()
    third_frame()
    
    
def third_frame():

    third_frame.frm = Frame(root)
    third_frame.frm.pack(side=BOTTOM, padx=15, pady=15)

    third_frame.label3 = Label(root, text='Number of predicted beetle', font=('Roboto', 15), padx=15, pady=15)
    third_frame.label3.pack() 

    third_frame.lbl2 = Label(root, text=pest_counter(io.imread(show_image.fln)), font=('Roboto', 35), padx=30, pady=30)
    third_frame.lbl2.pack()

    third_frame.button4 = Button(third_frame.frm, text='Browes another Image', font=('Roboto', 15), command=destroy_third)
    third_frame.button4.pack(side=tk.LEFT, pady=15)

    third_frame.button5 = Button(third_frame.frm, text='Exit', font=('Roboto', 15), command=root.quit)
    third_frame.button5.pack(side=tk.LEFT, pady=15, padx=10)


def show_image():
    show_image.fln = filedialog.askopenfilename()
    show_image.img = Image.open(show_image.fln)
    show_image.img.thumbnail((300, 300))
    show_image.img = ImageTk.PhotoImage(show_image.img)
    second_frame.lbl.configure(image = show_image.img)
    second_frame.lbl.image = show_image.img
    show_image.button3 = Button(second_frame.frm, text='Predict', font=('Roboto', 15), command=destroy_second)
    show_image.button3.pack(side=tk.LEFT, pady=15, padx=10)


def destroy_first():
    landing.label1.destroy()
    landing.button1.destroy()
    landing.img.destroy()
    second_frame()


def second_frame():

    second_frame.frm = Frame(root)
    second_frame.frm.pack(side=BOTTOM, padx=15, pady=15)
    
    
    second_frame.label2 = Label(root, text='Upload an picture to predict', font=('Roboto', 15), padx=15, pady=15)
    second_frame.label2.pack()

    second_frame.lbl = Label(root)
    second_frame.lbl.pack()

    second_frame.button2 = Button(second_frame.frm, text='Browes Image', font=('Roboto', 15), command=show_image)
    second_frame.button2.pack(side=tk.LEFT, pady=15)


def landing():

    landing.label1 = Label(root, text='Welcome to Beetle Counter', font=('Roboto', 15), padx=15, pady=15)
    landing.label1.pack()
    

    load = Image.open('images\count.png')
    render = ImageTk.PhotoImage(load)
    landing.img = Label(image=render)
    landing.img.image = render
    landing.img.place(x= 180, y=120)
    


    landing.button1 = Button(root, text='To Count', font=('Roboto', 15), command=destroy_first)
    landing.button1.pack(side=tk.BOTTOM, pady=15)

landing()
root.mainloop()