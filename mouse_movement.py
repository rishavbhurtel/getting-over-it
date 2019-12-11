# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 00:42:53 2019

@author: Rishav
"""

import pyautogui

def mouse_current_position():  
    # Retursn two integes, the x and y of the mouse cursor's current position.
    currentMouseX, currentMouseY = pyautogui.position()

def mouse_movement():
    # Move the mouse to the x, y coordinates 100, 150.
    pyautogui.moveTo(100, 150) 