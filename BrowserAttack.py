import tkinter.ttk as ttk
import tkinter as tk
import JavaScript.URL
import JavaScript.XSS
class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        menubar=tk.Menu(self)
        self['menu']=menubar
        self.current=JavaScript.XSS.GUI(self)
        self.current.pack()
        jsmenu=tk.Menu(menubar)
        jsmenu.add_command(label='XSS', command=lambda:self.CS(JavaScript.XSS.GUI))
        jsmenu.add_command(label='URL', command=lambda:self.CS(JavaScript.URL.GUI))
        menubar.add_cascade(label='JavaScript', menu=jsmenu)
    def CS(self, function):
        self.current.destroy()
        self.current=function(self)
        self.current.pack(expand=True, fill='both')
    
GUI()
