from tkinter import Tk

class window(Tk):
    def __init__(self,size = "600x400"):
        super().__init__()
        self.title("Student Managment Program")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.geometry(size)
    def show(self):
        self.mainloop()