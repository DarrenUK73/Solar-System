import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import * 
import csv
import json

class JSONVar(tk.StringVar):
    """A TK variable that can hold dics and lists"""

    def __init__(self, *args, **kwargs):
        kwargs['value'] = json.dumps(kwargs.get('value'))
        super().__init__(*args, **kwargs)

    def set(self, value, *args, **kwargs):
        string = json.dumps(value)
        super().set(string, *args, **kwargs)

    def get(self, *args, **kwargs):
        string = super().get(*args, **kwargs)
        return json.loads(string)

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
        pass
        #print(self.planet) 


class Questions:
    
    def __init__(self, parent, *args, **kwargs):

        super().__init__(parent, *args, **kwargs)

        # self.questionno = questionno
        # self.questiontext = questiontext
        # self.answertext = answertext

    def buildanswer(self, state):
        data = {key : var.get() for key, var in self._vars.items()}
        self.data_var.set(data)
        if state==True:
            selected_questions[self.questionno]=self.answertext
        else:
            del selected_questions[self.questionno] #stack overflow

        # if bool(selected_questions)==False: #bool - stack overflow
        #     submit_btn.configure(state=DISABLED) #state - stack overflow
        # else:
        #     submit_btn.configure(state=NORMAL)

def completeanswer(planet_ind):
    answerstring = ''
    answertext1 =''
    answertext2 =''
    sorted_questions = dict(sorted(selected_questions.items()))
    planet_data = planets[planet_ind].getanswers()
    qu_keys = list(sorted_questions.keys())
    qu_ind = ''
    
    for i in range(len(qu_keys)):
        qu_ind = str(qu_keys[int(i)])
        answertext1 = sorted_questions[qu_ind]
        answertext2 = planet_data[int(qu_ind)-1]
        answerstring = answerstring+answertext1+' '+answertext2+'\n'
    
    return answerstring

class CheckButton(tk.Frame):
    def __init__(
        self, parent, label, inp_cls,
        inp_var, *args, **kwargs
    ):
        super().__init__(parent, *args, **kwargs)
        
        self.checkbutton = tk.Checkbutton(self, text=label, variable=inp_var, anchor='w')
        self.checkbutton.grid(row=0, column=1, sticky='we')

class MyForm(tk.Frame):
    
    def __init__(self, parent, data_var, 
        *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.data_var = data_var
            
        self._vars = {
        'qu1': tk.BooleanVar(self),
        'qu2' :tk.BooleanVar(self),
        'qu3' :tk.BooleanVar(self),
        'qu4' :tk.BooleanVar(self),
        'qu5' :tk.BooleanVar(self),
        'qu6' :tk.BooleanVar(self),
        'planet' :tk.StringVar(self),
        }

        planet_dict = {}
        for i in range(0,len(planets)):
            planet_dict[planets[i].planet] = i

        planet_inp = ttk.Combobox(self, textvariable=self._vars['planet'], values=list(planet_dict.keys()))
        planet_inp.grid(row=4, column=2, sticky=tk.W + tk.E, padx=25)
        
        CheckButton(self, questions[0].questiontext, tk.Checkbutton, self._vars['qu1']).grid(sticky='we')
        
        CheckButton(self, questions[1].questiontext, tk.Checkbutton, self._vars['qu2']).grid(sticky='we')
        
        CheckButton(self, questions[2].questiontext, tk.Checkbutton, self._vars['qu3']).grid(sticky='we')
        
        CheckButton(self, questions[3].questiontext, tk.Checkbutton, self._vars['qu4']).grid(sticky='we')
        
        CheckButton(self, questions[4].questiontext, tk.Checkbutton, self._vars['qu5']).grid(sticky='we')
        
        CheckButton(self, questions[5].questiontext, tk.Checkbutton, self._vars['qu6']).grid(sticky='we')
                            
        #tk.Button(self, text='Submit', command=self._on_submit).grid()
        submit_btn = tk.Button(self, text='OK')
        submit_btn.grid(row=20, column=0, pady=150)
        submit_btn.configure(command=self._on_click)
        
        cancel_btn = tk.Button(self, text='Cancel')
        cancel_btn.grid(row=20, column=1, pady=150)
        cancel_btn.configure(command=self._on_cancel)

        exit_btn = tk.Button(self, text='Exit')
        exit_btn.grid(row=20, column=2, pady=150)
        exit_btn.configure(command=self.destroy)

    def _on_click(self):
        data = {key : var.get() for key, var in self._vars.items()}
        print(data)
        self.data_var.set(data)
        self.questions.buildanswer(data)

    def _on_submit(self, pl_dict,selected_planet):
        data = {key : var.get() for key, var in self._vars.items()}
        self.data_var.set(data)
    #check the planet is valid before proceeding
        if self._vars['planet'].get() in list(pl_dict.keys()):
            ind = pl_dict[self._vars['planet'].get()]

            answerstring = completeanswer(ind)

            messagebox.showinfo(
            title='Answers',
            message=f'Here is the result of you enquiry for planet {selected_planet}',
            detail=answerstring
        )

        else:
            messagebox.showerror(
            title='Invalid Planet Name',
            message=self._vars['planet'].get()+' is not a planet in the Solar System',
            detail='Please select from the list'
        )
        return False

    def _on_cancel(self):
        selected_questions.clear() #stack overflow
        #submit_btn.configure(state=DISABLED)
        self._vars['qu1'].set(False)
        self._vars['qu2'].set(False)
        self._vars['qu3'].set(False)
        self._vars['qu4'].set(False)
        self._vars['qu5'].set(False)
        self._vars['qu6'].set(False)
        self._vars['planet'].set('Mercury')

class SolarSystem(tk.Tk):
    """A simple form application"""
    from tkinter import ttk
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #print(self)
        self.jsonvar = JSONVar(self)
        self.outpur_var = tk.IntVar(self)
        self.geometry("640x480+300+300")
        self.title("Solar System Enquiry")
        self.resizable(False,False)
        
        title = tk.Label(self, text='Solar System Knowledge Base', font=('Arial 16 bold'),bg='black',fg='blue')
        title.grid(columnspan=2)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        MyForm(self, self.jsonvar).grid(sticky='nsew')
        #tk.IntVar(self, textvariable=self.outpur_var).grid(sticky='ew')
        
        self.jsonvar.trace_add('write', self._on_data_change)

    def _on_data_change(self, *args, **kwargs):
        data = self.jsonvar.get()
        output = ''.join([
            f'{key} = {value}\n'
            for key, value in data.items()
        ])
        self.outpur_var.set(output)


if __name__ == "__main__":
    
    selected_questions = {}
    planets = []
    questions = []

    ####### https://blog.finxter.com/ ########
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