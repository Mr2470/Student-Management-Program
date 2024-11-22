from ttkbootstrap import Frame
from .Window import window
from .login import login

class Cordinator:
    def __init__(self):
        self.window = window()

        self.Frames = {}
        self.AddFrame("login", login(self.window,self))

        self.window.show()

    def AddFrame(self, FrameName, Frame):
        self.Frames[FrameName] = Frame
        self.Frames[FrameName].grid(row=0, column=0, sticky="wnes")

    def switch(self,FrameName):
        Frame = self.Frames[FrameName]
        Frame.tkraise()
        return Frame