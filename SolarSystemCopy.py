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

    def getanswers(self):
        planet_data = [self.mass,self.noofmoons,self.distance,self.area,self.orbit,self.moonlist]
        return planet_data
    
    def validplanet(self):
        print(self.planet) 


class Questions:
    def __init__(self, questionno, questiontext,answertext):
        self.questionno = questionno
        self.questiontext = questiontext
        self.answertext = answertext

    def buildanswer(self, state):
        if state==True:
            selected_questions[self.questionno]=self.answertext
        else:
            del selected_questions[self.questionno] #stack overflow

        if bool(selected_questions)==False: #bool - stack overflow
            submit_btn.configure(state=DISABLED) #state - stack overflow
        else:
            submit_btn.configure(state=NORMAL)

####### https://blog.finxter.com/ ########

#draw main screen
root = tk.Tk()
root.title('Solar System Enquiry')
root.geometry('640x480+300+300')
root.resizable(False,False)
title = tk.Label(root, text='Solar System Knowledge Base', font=('Arial 16 bold'),bg='black',fg='blue')
title.grid(columnspan=2)

selected_questions = {}
planets = []
questions = []

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


def on_submit():
    inputplanet = planet_var.get()
    #inputplanet.validplanet(inputplanet)

    #check the planet is valid before proceeding
    if planet_var.get() in list(planet_dict.keys()):
        ind = planet_dict[planet_var.get()]

        sorted_questions = dict(sorted(selected_questions.items()))
        planet_data = planets[ind].getanswers()
        print(planet_data)
        qu_keys = list(sorted_questions.keys())
        answerstring = ''
        answertext1 =''
        answertext2 =''
        qu_ind = ''
        for i in range(len(qu_keys)):
            qu_ind = str(qu_keys[int(i)])
            answertext1 = sorted_questions[qu_ind]
            answertext2 = planet_data[int(qu_ind)-1]
            answerstring = answerstring+answertext1+' '+answertext2+'\n'

        messagebox.showinfo(
            title='Answers',
            message=f'Here is the result of you enquiry for planet {planet_var.get()}',
            detail=answerstring
        )

    else:
        messagebox.showerror(
            title='Invalid Planet Name',
            message=planet_var.get()+' is not a planet in the Solar System',
            detail='Please select from the list'
        )
        return False
    
def on_cancel():
    selected_questions.clear() #stack overflow
    submit_btn.configure(state=DISABLED)
    qu1_var.set(False)
    qu2_var.set(False)
    qu3_var.set(False)
    qu4_var.set(False)
    qu5_var.set(False)
    qu6_var.set(False)
    planet_var.set('Mercury')

def on_click(state,qu_ind):
    questions[qu_ind].buildanswer(state)
    
    # if bool(selected_questions)==False: #bool - stack overflow
    #     submit_btn.configure(state=DISABLED) #state - stack overflow
    # else:
    #     submit_btn.configure(state=NORMAL)

   
# Screen, widgets and message boxes from
# Python GUI Programming with Tkinter - Alan D. Moore

#initialise the combo box 
planet_var = tk.StringVar(value='Mercury')
planet_label = tk.Label(root, text='Please select a planet')

#add choices
planet_dict = {}
for i in range(0,len(planets)):
    planet_dict[planets[i].planet] = i

planet_inp = ttk.Combobox(root, textvariable=planet_var, values=list(planet_dict.keys()))

planet_label.grid(row=4, sticky=tk.W, pady=10)
planet_inp.grid(row=4, column=2, sticky=tk.W + tk.E, padx=25)

qu1_var = tk.BooleanVar()
qu1 = tk.Checkbutton(root, variable=qu1_var, text=questions[0].questiontext, anchor='w', 
                     command=lambda:on_click(qu1_var.get(),0))
qu1.grid(row=7, columnspan=2, sticky='we')

qu2_var = tk.BooleanVar()
qu2 = tk.Checkbutton(root, variable=qu2_var, text=questions[1].questiontext, anchor='w', 
                     command=lambda: on_click(qu2_var.get(),1))
qu2.grid(row=8, columnspan=2, sticky='we')

qu3_var = tk.BooleanVar()
qu3 = tk.Checkbutton(root, variable=qu3_var, text=questions[2].questiontext, anchor='w', 
                     command=lambda:on_click(qu3_var.get(),2))
qu3.grid(row=9, columnspan=2, sticky='we')

qu4_var = tk.BooleanVar()
qu4 = tk.Checkbutton(root, variable=qu4_var, text=questions[3].questiontext, anchor='w', 
                     command=lambda:on_click(qu4_var.get(),3))
qu4.grid(row=10, columnspan=2, sticky='we')

qu5_var = tk.BooleanVar()
qu5 = tk.Checkbutton(root, variable=qu5_var, text=questions[4].questiontext, anchor='w', 
                     command=lambda:on_click(qu5_var.get(),4))
qu5.grid(row=11, columnspan=2, sticky='we')

qu6_var = tk.BooleanVar()
qu6 = tk.Checkbutton(root, variable=qu6_var, text=questions[5].questiontext, anchor='w', 
                     command=lambda:on_click(qu6_var.get(),5))
qu6.grid(row=12, columnspan=2, sticky='we')

#### lambda from stack overflow #####

submit_btn = tk.Button(root, text='OK')
submit_btn.grid(row=20, column=0, pady=25)
submit_btn.configure(command=on_submit, state=DISABLED)

cancel_btn = tk.Button(root, text='Cancel')
cancel_btn.grid(row=20, column=1, pady=25)
cancel_btn.configure(command=on_cancel)

exit_btn = tk.Button(root, text='Exit')
exit_btn.grid(row=20, column=2, pady=25)
exit_btn.configure(command=root.destroy)

root.mainloop()