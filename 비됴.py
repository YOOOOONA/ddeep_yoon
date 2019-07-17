# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 23:15:25 2019

@author: 융
"""

import tkinter
import cv2

class App:
    def __init__(self, window, window_title, video_source='avengers_endgame.mov'):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # open video source
        self.vid = MyVideoCapture(video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()


        self.window.mainloop()