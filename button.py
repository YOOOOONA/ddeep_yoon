# -*- coding: utf-8 -*-
"""
Created on Sun May 26 21:27:24 2019

@author: kyeoj
"""

import augmentation_new
import train_main
import os,sys,time
os.chdir(os.path.dirname(__file__))
from tkinter import *
import tkinter as tk
import classifier


def click_button(button_flag, feature_list):

    def click1():    
        """
        respond to the button1 click
        """
        # toggle button colors as a test
        if (button_flag[1] % 2 ==1):
            button1.config(bg="white")
            if button_flag[1] == 1:
                aug_img = augmentation_new.Make_Data('C:/Facenet-Real-time-Tensorflow/avengers/evans/evans.gif', 'evans')
                
                train_main.image_train(pre_image)
            button_flag[1] +=1
            
        elif (button_flag[1] %2 ==0):
            button1.config(bg="green")
            button_flag[1] +=1 
            
            
            
    def click2():
        """
        respond to the button2 click
        """
        # toggle button colors as a test
        if (button_flag[2] % 2 ==1):
            button2.config(bg="white")
            if button_flag[2] == 1:
                aug_img = augmentation_new.Make_Data('C:/Facenet-Real-time-Tensorflow/avengers/hermsworth/hermsworth.gif', 'hermsworth')
                pre_image.append(aug_img)
                train_main.image_train(pre_image)
            button_flag[2] +=1
            
        elif(button_flag[2] %2 ==0):
            button2.config(bg="green")
            button_flag[2] += 1
            
    def click3():
        """
        respond to the button3 click
        """
        # toggle button colors as a test
        if (button_flag[3]%2==1):
            button3.config(bg="white")
            if button_flag[3] == 1:
                aug_img = augmentation_new.Make_Data('C:/Facenet-Real-time-Tensorflow/avengers/jeremy/jeremy.gif', 'jeremy')
                pre_image.append(aug_img)
                train_main.image_train(pre_image)
            button_flag[3] += 1
                
        
        elif(button_flag[3] %2 ==0):
            button3.config(bg="green")
            button_flag[3] += 1    
   
    def click4():
        """
        respond to the button4 click
        """    
        # toggle button colors as a test
        if (button_flag[4]%2 ==1):
            button4.config(bg="white")
            if button_flag[4] == 1:
                aug_img = augmentation_new.Make_Data('C:/Facenet-Real-time-Tensorflow/avengers/mark/mark.gif', 'mark')
                pre_image.append(aug_img)
                train_main.image_train(pre_image)
            button_flag[4] += 1
                
        
        elif(button_flag[4]%2 ==0):
            button4.config(bg="green")
            button_flag[4] += 1
            
            
    def click5():
        """
        respond to the button5 click
        """    
        # toggle button colors as a test
        if (button_flag[5] %2 ==1):
            button5.config(bg="white")
            if button_flag[5] == 1:
                aug_img = augmentation_new.Make_Data('C:/Facenet-Real-time-Tensorflow/avengers/olsen/olsen.gif', 'olsen')
                pre_image.append(aug_img)
                train_main.image_train(pre_image)
            button_flag[5] += 1
            
        elif(button_flag[5] %2 ==0):
            button5.config(bg="green")
            button_flag[5] += 1
            
    
    root = tk.Tk()
    # create a frame and pack it
    frame1 = tk.Frame(root)
    frame1.pack(side=tk.TOP, fill=tk.X)
    
    # pick a (small) image file you have in the working directory ...
    filename1 = os.path.join(os.getcwd(),'avengers/evans/evans.gif')
    photo1 = tk.PhotoImage(file=filename1)
    # create the image button, image is above (top) the optional text
    button1 = tk.Button(frame1, compound=tk.TOP, width=200, height=200, image=photo1,
                        text="optional text", bg='green', command=click1)
    button1.pack(side=tk.LEFT, padx=4, pady=50)
    # save the button's image from garbage collection (needed?)
    button1.image = photo1

    filename2 = os.path.join(os.getcwd(), 'avengers/hermsworth/hermsworth.gif')
    photo2 = tk.PhotoImage(file=filename2)
    # create the image button, image is above (top) the optional text
    button2 = tk.Button(frame1, compound=tk.TOP, width=200, height=200, image=photo2,
                        text="optional text", bg='green', command=click2)
    button2.pack(side=tk.LEFT, padx=4, pady=50)
    # save the button's image from garbage collection (needed?)
    button2.image = photo2

    filename3= os.path.join(os.getcwd(), 'avengers/jeremy/jeremy.gif')
    photo3 = tk.PhotoImage(file=filename3)
    # create the image button, image is above (top) the optional text
    button3 = tk.Button(frame1, compound=tk.TOP, width=200, height=200, image=photo3,
                        text="optional text", bg='green', command=click3)
    button3.pack(side=tk.LEFT, padx=4, pady=50)
    # save the button's image from garbage collection (needed?)
    button3.image = photo3
    
    filename4= os.path.join(os.getcwd(), 'avengers/mark/mark.gif')
    photo4 = tk.PhotoImage(file=filename4)
    # create the image button, image is above (top) the optional text
    button4 = tk.Button(frame1, compound=tk.TOP, width=200, height=200, image=photo4,
                        text="optional text", bg='green', command=click4)
    button4.pack(side=tk.LEFT, padx=4, pady=50)
    # save the button's image from garbage collection (needed?)
    button4.image = photo4

    fileneme5 = os.path.join(os.getcwd(), 'avengers/olsen/olsen.gif')
    photo5 = tk.PhotoImage(file=filename5)
    # create the image button, image is above (top) the optional text
    button5 = tk.Button(frame1, compound=tk.TOP, width=200, height=200, image=photo5,
                        text="optional text", bg='green', command=click5)
    button5.pack(side=tk.LEFT, padx=4, pady=50)
    # save the button's image from garbage collection (needed?)
    button5.image = photo5
    # start the event loop
    root.mainloop()