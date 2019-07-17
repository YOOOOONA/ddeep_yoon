# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:38:12 2019

@author: 융
"""

import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk

window = tk.Tk()

video_name = "avengers_endgame.mov" #This is your video file path
video = imageio.get_reader(video_name)

window.title("실시간 얼굴 인식")
window.geometry("700x500+100+100")

def stream(label):
    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image

my_label = tk.Label(window)
thread = threading.Thread(target=stream, args=(my_label, ))
thread.daemon = 1
thread.start()

window.mainloop()