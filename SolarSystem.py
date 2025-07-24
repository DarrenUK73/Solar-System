import tkinter as tk
from tkinter import * 
from tkinter.ttk import * 
from time import strftime

class Planets:
    def __init__(self, name="", mass=0, distance=0, moons=""): 
        self.name = name
        self.mass = mass
        self.distance = distance
        self.moons = moons

class Moons:
    def __init__(self, name="", planet=""): 
        self.name = name
        self.planet = planet

def moon(arg):
    arg = Moons("The Moon", "Earth")
    print(f'{arg.name} orbits the planet {arg.planet}')
    #return()

 
# Definition of the main application window
window = tk.Tk()
window.title("Solar System Knowledge Base")
window.geometry("800x600")
 
# Definition of a menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)
 
# Create a functions1 menu
functions1 = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Functions1", menu=functions1)
functions1.add_command(label='test',command=lambda: moon("themoon"))
 
# Create a functions2 menu
functions2 = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Functions2", menu=functions2)
 
# Start the main event loop
window.mainloop()

