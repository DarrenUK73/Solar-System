import tkinter as tk
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
    
class LabelInput(tk.Frame):
    """A Label and input combined together"""

    def __init__(
        self, parent, label, inp_cls,
        inp_args, *args, **kwargs
    ):
        super().__init__(parent, *args, **kwargs)

        self.label = tk.Label(self, text=label, anchor='w')
        self.input = inp_cls(self, **inp_args)

        self.columnconfigure(0, weight=1)
        self.label.grid(sticky=tk.E +tk.W)
        self.input.grid(row=0, column=1, sticky=tk.E + tk.W)

class MyForm(tk.Frame):

    def __init__(self, parent, data_var, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.data_var = data_var
            
        self._vars = {
        'name': tk.StringVar(self),
        'age' :tk.IntVar(self, value=2)
        }

        LabelInput(
            self, 'Name', tk.Entry,
            {'textvariable' : self._vars['name']}
            ).grid(sticky=tk.E + tk.W)
        LabelInput(
            self, 'Age', tk.Spinbox,
            {'textvariable' : self._vars['age'], 'from_' : 10, 'to' : 150}
            ).grid(sticky=tk.E + tk.W)
            
        tk.Button(self, text='Submit', command=self._on_submit).grid()

    def _on_submit(self):
            data = {key : var.get() for key, var in self._vars.items()}
            self.data_var.set(data)

class Application(tk.Tk):
    """A simple form application"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.jsonvar = JSONVar(self)
        self.outpur_var = tk.StringVar(self)

        tk.Label(self, text='Please fill the form').grid(sticky='ew')
        MyForm(self, self.jsonvar).grid(sticky='nsew')
        tk.Label(self, textvariable=self.outpur_var).grid(sticky='ew')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.jsonvar.trace_add('write', self._on_data_change)

    def _on_data_change(self, *args, **kwargs):
        data = self.jsonvar.get()
        output = ''.join([
            f'{key} = {value}\n'
            for key, value in data.items()
        ])
        self.outpur_var.set(output)

        

if __name__ == "__main__":
    app = Application()
    app.mainloop()
    
