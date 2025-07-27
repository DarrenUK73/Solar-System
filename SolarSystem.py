import tkinter as tk
from tkinter import * 
from tkinter import messagebox
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
    def __init__(self, questionno, questiontext):
        self.questionno = questionno
        self.questiontext = questiontext
        
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

    if planet_var.get() in planet_choices:

        answers = [qu1_var.get(),qu2_var.get(),qu3_var.get()]
        answer_text = []
        result = tk.Tk()

        result.title('Answers')
        result.geometry('640x480+300+300')
        result.resizable(False,False)
        title = tk.Label(result, text='Answers', font=('Arial 16 bold'),bg='black',fg='blue')
        title.grid(columnspan=2)

        for i in range(0,len(planets)):
            if planet_var.get() == planets[i].name:
                answer_text= [planets[i].mass,planets[i].moons]

        for i in range(0,len(answers)):
            if answers[i] == True:
                print(answer_text[i])

    else:
        messagebox.showerror(
            title='Invalid Planet Name',
            message=planet_var.get()+' is not a planet in the Solar System',
            detail='Please select from the list'
        )
        return False
    
def on_cancel():
    pass

def on_exit():
    pass

#Python GUI Programming with Tkinter - Alan D. Moore

planet_var = tk.StringVar(value='Mercury')
planet_label = tk.Label(root, text='Please select a planet')

#add choices
planet_choices = []

for i in range(0,len(planets)):
    planet_choices.append(planets[i].name)

planet_inp = ttk.Combobox(root, textvariable=planet_var, values=planet_choices)

planet_label.grid(row=4, sticky=tk.W, pady=10)
planet_inp.grid(row=4, column=2, sticky=tk.W + tk.E, padx=25)

qu1_var = tk.BooleanVar()
qu1 = tk.Checkbutton(root, variable=qu1_var, text=questions[0].questiontext, anchor='w')
qu1.grid(row=7, columnspan=2, sticky='we')

qu2_var = tk.BooleanVar()
qu2 = tk.Checkbutton(root, variable=qu2_var, text=questions[1].questiontext, anchor='w')
qu2.grid(row=8, columnspan=2, sticky='we')

qu3_var = tk.BooleanVar()
qu3 = tk.Checkbutton(root, variable=qu3_var, text=questions[2].questiontext, anchor='w')
qu3.grid(row=9, columnspan=2, sticky='we')


submit_btn = tk.Button(root, text='OK')
submit_btn.grid(row=99, column=0, pady=250)
submit_btn.configure(command=on_submit)

cancel_btn = tk.Button(root, text='Cancel')
cancel_btn.grid(row=99, column=1, pady=250)
cancel_btn.configure(command=on_cancel)

exit_btn = tk.Button(root, text='Exit')
exit_btn.grid(row=99, column=2, pady=250)
exit_btn.configure(command=on_exit)

root.mainloop()