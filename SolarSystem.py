import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter.ttk import * 
from time import strftime
import csv

class Planets:
    def __init__(self, name="", mass=0, moons=""): 
        self.name = name
        self.mass = mass
        self.moons = moons

####### https://blog.finxter.com/ ########

planets = []

with open('Planets.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        planets.append(Planets(row['name'], row['mass'], row['moons']))
print(planets)

############################################

print(planets[1].name)

#class Moons:
#    def __init__(self, name="", planet=""): 
#        self.name = name
#        self.planet = planet

#def moon(arg):
#    arg = Moons("The Moon", "Earth")
#    print(f'{arg.name} orbits the planet {arg.planet}')
#    #return()

def on_submit():
    """to be run when the user submits the form"""
    planet = planet_var.get()
    question1 = question1_var.get()
    question2 = question2_var.get()
    question3 = question3_var.get()


#Python GUI Programming with Tkinter - Alan D. Moore
root = tk.Tk()

root.title('Solar System Enquiry')
root.geometry('640x480+300+300')
root.resizable(False,False)

title = tk.Label(root, text='Solar System Knowledge Base', font=('Arial 16 bold'),bg='black',fg='blue')

planet_var = tk.StringVar(value='Mercury')
planet_label = tk.Label(root, text='Please select a planet')

#add choices
planet_choices = ['Mercury', 'Venus', 'Earth', 'Mars', 'Saturn', 'Jupiter', 'Neptune', 'Uranus'] 

#planet_inp = ttk.Combobox(root, textvariable=planet_var, values=['Mercury', 'Venus', 'Earth', 'Mars', 'Saturn', 'Jupiter', 'Neptune', 'Uranus'])
planet_inp = ttk.Combobox(root, textvariable=planet_var, values=planet_choices)

question1_var = tk.BooleanVar()
question1_inp = tk.Checkbutton(root, variable=question1_var, text='What is the planet mass?', anchor='w')

question2_var = tk.BooleanVar()
question2_inp = tk.Checkbutton(root, variable=question2_var, text='What is the number of moons?',anchor='w')

question3_var = tk.BooleanVar()
question3_inp = tk.Checkbutton(root, variable=question3_var, text='What is the distance from the Sun?',anchor='w')

submit_btn = tk.Button(root, text='Submit Questions')

title.grid(columnspan=2)

planet_label.grid(row=4, sticky=tk.W, pady=10)
planet_inp.grid(row=4, column=2, sticky=tk.W + tk.E, padx=25)

question1_inp.grid(row=7, columnspan=2, sticky='we') 
question2_inp.grid(row=8, columnspan=2, sticky='we') 
question3_inp.grid(row=9, columnspan=2, sticky='we')


submit_btn.grid(row=99)

submit_btn.configure(command=on_submit)

root.mainloop()