from ttkbootstrap import Frame, Label, Entry, Button, END
from tkinter import messagebox

class auth(Frame):
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

        self.login_button = Button(self, text="login", command=self.login_button)
        self.login_button.grid(row=3, column=1, pady=(0, 10), sticky="w")

        self.Register_button = Button(self, text="Register", command=self.Register)
        self.Register_button.grid(row=3, column=1, pady=(0, 10), sticky="e",padx=(0, 20))

    def login_button(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        print(f"{username=}\n{password=}")

    def Register(self):
        self.mainveiw.switch("register")

        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Register Page")
        self.header.grid(row=0, column=1, pady=10, sticky="w")


        self.fname_label = Label(self, text="First Name")
        self.fname_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="w")

        self.fname_entry = Entry(self)
        self.fname_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.lname_label = Label(self, text="Last Name")
        self.lname_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="w")

        self.lname_entry = Entry(self)
        self.lname_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="w")

        self.username_entry = Entry(self)
        self.username_entry.grid(row=3, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=4, column=0, pady=(0, 10), padx=10, sticky="w")

        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=4, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        # command needs to change
        self.register_button = Button(self, text="Register", command=self.register_button)
        self.register_button.grid(row=5, column=1, pady=(0, 10), sticky="w")

        # command needs to change
        self.Login_button = Button(self, text="Login", command=self.Register)
        self.Login_button.grid(row=5, column=1, pady=(0, 10), sticky="e",padx=(0, 20))

    def register_button(self):
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        print(f"{fname=}\n{lname=}\n{username=}\n{password=}")


    