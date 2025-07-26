import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter.ttk import * 
import csv

root = tk.Tk()

root.title('Solar System Enquiry')
root.geometry('640x480+300+300')
root.resizable(False,False)
title = tk.Label(root, text='Solar System Knowledge Base', font=('Arial 16 bold'),bg='black',fg='blue')
title.grid(columnspan=2)

class Planets:
    def __init__(self, name="", mass=0, moons=""): 
        self.name = name
        self.mass = mass
        self.moons = moons

class Questions:
    def __init__(self, questionno=0, questiontext=""):
        boolvar=tk.BooleanVar
        self.questionno = questionno
        self.questiontext = questiontext
        self.cb = tk.Checkbutton(root, variable=boolvar, text=questiontext, anchor='w') #stack overflow
        self.cb.grid(row=int(questionno)+7, columnspan=2, sticky='we') #stack overflow

####### https://blog.finxter.com/ ########

#read in CSVs and add class instances

planets = []
questions = []

with open('Planets.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        planets.append(Planets(row['name'], row['mass'], row['moons']))

with open('planetquestions.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        questions.append(Questions(row['questionno'], row['questiontext']))

############################################


def on_submit():
    #to be run when the user submits the form
    planet = planet_var.get()
    # question1 = question1_var.get()
    # question2 = question2_var.get()
    # question3 = question3_var.get()


#Python GUI Programming with Tkinter - Alan D. Moore

planet_var = tk.StringVar(value='Mercury')
planet_label = tk.Label(root, text='Please select a planet')

#add choices
planet_choices = []

for i in range(0,len(planets)):
    planet_choices.append(planets[i].name)

planet_inp = ttk.Combobox(root, textvariable=planet_var, values=planet_choices)

submit_btn = tk.Button(root, text='Submit Questions')

planet_label.grid(row=4, sticky=tk.W, pady=10)
planet_inp.grid(row=4, column=2, sticky=tk.W + tk.E, padx=25)

submit_btn.grid(row=99)

submit_btn.configure(command=on_submit)

root.mainloop()