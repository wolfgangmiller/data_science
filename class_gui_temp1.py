# Program: Class Based GUI
# Author: Maya Name
# Creation date 05/11/2019
# Revsion date
# Description: Single window class-based Tkinter window template

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class main_frm(tk.Frame): # Container frame for main window

    def __init__(self, parent, *args, **kwargs):
        # constructor allows the use of the same args as the subclassed tk.Frame
        super().__init__(parent, *args, **kwargs)

        # Create widget variables
        self.name_str = tk.StringVar()
        self.greeting_str = tk.StringVar(value='What\' your name')

        def on_change():
            if self.name_str.get().strip():
                self.greeting_str.set('Hello there, ' + self.name_str.get())
            else:
                self.greeting_str.set('Hello there, stranger.')

        # Create pack and widgets  
        name_lbl = ttk.Label(self, text = 'Name: ')
        name_lbl.grid(row = 0, column = 0, sticky = tk.W)

        name_ent = ttk.Entry(self, textvariable = self.name_str)
        name_ent.grid(row = 0, column = 1, sticky = (tk.W + tk.E))

        greet_btn = ttk.Button(self, text = 'Greeting', command = on_change)
        greet_btn.grid(row = 0, column = 2, sticky = tk.E)

        greeting_lbl = ttk.Label(self, textvariable = self.greeting_str)
        greeting_lbl.grid(row = 1, column = 0, columnspan = 3)

        self.columnconfigure(1, weight = 1)




class App(tk.Tk):  # Inheriting from Tk class

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)  # Initializing the inherited class

        # Define application properties
        self.title('Class Based GUI')
        self.geometry('300x100')
        tk.Tk.iconbitmap(self, default='./wolftrack.ico')
        self.resizable(width = False, height = False)

        # Add widget frame to application
        main_frm(self).grid(sticky = (tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight = 1)


def main():
    prog_app = App()
    prog_app.mainloop()


if __name__ == '__main__': main()
