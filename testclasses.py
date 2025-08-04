import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import * 
import csv

class Planets:
    def __init__(self, planet="", mass=0, noofmoons=0, distance="", area="", orbit="", moonlist=[]): 
        self.planet = planet
        self.mass = mass
        self.noofmoons = noofmoons
        self.distance = distance
        self.area = area
        self.orbit = orbit
        self.moonlist = moonlist

class Questions:
    def __init__(self, questionno, questiontext,answertext):
        self.questionno = questionno
        self.questiontext = questiontext
        self.answertext = answertext


class CheckButton(tk.Frame):
    def __init__(
        self, parent, label, inp_cls,
        inp_args, *args, **kwargs
    ):
        super().__init__(parent, *args, **kwargs)

        self.checkbutton = tk.Checkbutton(self, text=label, anchor='w')
        self.checkbutton.grid(row=0, column=1, sticky='we')

class MyForm(tk.Frame):
    
    def __init__(self, parent, data_var, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.data_var = data_var
            
        self._vars = {
        'qu1': tk.BooleanVar(self),
        'qu2' :tk.BooleanVar(self),
        'qu3' :tk.BooleanVar(self),
        'qu4' :tk.BooleanVar(self),
        'qu5' :tk.BooleanVar(self),
        'qu6' :tk.BooleanVar(self),
        'planet' :tk.StringVar(self)
        }

        planet_inp = ttk.Combobox(self, textvariable=self._vars['planet'], values=list(['Mercury','Venus','Earth']))
        planet_inp.grid(row=4, column=2, sticky=tk.W + tk.E, padx=25)
        
        CheckButton(
            self, questions[0].questiontext, tk.Checkbutton,
            {'textvariable' : self._vars['qu1']}
            ).grid(sticky='we')
        CheckButton(
            self, questions[1].questiontext, tk.Checkbutton,
            {'textvariable' : self._vars['qu2']}
            ).grid(sticky='we')
        CheckButton(
            self, questions[2].questiontext, tk.Checkbutton,
            {'textvariable' : self._vars['qu3']}
            ).grid(sticky='we')
        CheckButton(
            self, questions[3].questiontext, tk.Checkbutton,
            {'textvariable' : self._vars['qu4']}
            ).grid(sticky='we')
        CheckButton(
            self, questions[4].questiontext, tk.Checkbutton,
            {'textvariable' : self._vars['qu5']}
            ).grid(sticky='we')
        CheckButton(
            self, questions[5].questiontext, tk.Checkbutton,
            {'textvariable' : self._vars['qu6']}
            ).grid(sticky='we')
            
        tk.Button(self, text='Submit', command=self._on_submit).grid()

    def _on_submit(self):
            data = {key : var.get() for key, var in self._vars.items()}
            self.data_var.set(data)

class SolarSystem(tk.Tk):
    """A simple form application"""
    from tkinter import ttk

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("640x480+300+300")
        self.title("Solar System Enquiry")
        self.resizable(False,False)
        #self.jsonvar = JSONVar(self)
        self.outpur_var = tk.StringVar(self)
        
        title = tk.Label(self, text='Solar System Knowledge Base', font=('Arial 16 bold'),bg='black',fg='blue')
        title.grid(columnspan=2)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        MyForm(self, "Test").grid(sticky='nsew')


if __name__ == "__main__":
    ####### https://blog.finxter.com/ ########
    planets =[]
    questions=[]
#read in CSVs and add class instances
    with open('Planets.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            planets.append(Planets(row['planet'], row['mass'], row['noofmoons'], row['distance'], row['area'],row['orbit'],row['moonlist']))

    with open('planetquestions.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            questions.append(Questions(row['questionno'], row['questiontext'], row['answertext']))

############################################
    app = SolarSystem()
    app.mainloop()
