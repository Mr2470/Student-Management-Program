from ttkbootstrap import Frame, Label, Entry, Button, END
from tkinter import messagebox

class login(Frame):
    def __init__(self, window, mainveiwer):
        super().__init__(window)
        self.mainveiw = mainveiwer
        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Login Page")
        self.header.grid(row=0, column=1, pady=10, sticky="w")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="w")

        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.login_button = Button(self, text="login", command=self.login)
        self.login_button.grid(row=3, column=1, pady=(0, 10), sticky="w")

        self.Register_button = Button(self, text="Register", command=self.Register)
        self.Register_button.grid(row=3, column=1, pady=(0, 10), sticky="e",padx=(0, 20))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
    def Register(self):
        self.mainveiw.switch("Register")