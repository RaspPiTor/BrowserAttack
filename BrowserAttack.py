import sys
import JavaScript.URL as URL
import JavaScript.XSS as XSS

if sys.version_info.major == 2:
    import Tkinter as tk
    #import ttk
else:
    #import tkinter.ttk as ttk
    import tkinter as tk

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        menubar = tk.Menu(self)
        self['menu'] = menubar
        self.current = URL.GUI(self)
        self.current.pack()
        jsmenu = tk.Menu(menubar)
        menubar.add_cascade(label='JavaScript', menu=jsmenu)
        #Create Screen
        self.current.destroy()
        self.current = function(self)
        self.current.pack(expand=True, fill='both')

GUI().mainloop()
