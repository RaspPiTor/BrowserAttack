import tkinter.ttk as ttk
import tkinter as tk


class GUI(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        ttk.Label(self, text='Javascript:').grid(column=0,row=2,sticky='nw')
        self.js=tk.Text(self, height=10)
        self.js.grid(column=1, row=2, sticky='nw')
        ttk.Button(self, text='Generate',
                   command=self.generate).grid(column=0, row=3,sticky='nw')
        self.result=tk.Text(self, height=10)
        self.result.grid(column=1, row=3, sticky='nw')
    def generate(self):
        self.result.delete('1.0', 'end')
        result=self.js.get("1.0",'end-1c')
        fakeurl=self.url.get("1.0",'end-1c')
        result=URL2JS(result, fakeurl=fakeurl)
        self.result.insert('end', result)
