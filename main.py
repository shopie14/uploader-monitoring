from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from src.form import login, register

class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Monja Uploader")
        self.state('zoomed')
        self.resizable(0, 0)
        self.geometry("400x400")
        self.minsize(750, 650)
        self.maxsize(750, 650)
        self.iconphoto(True, PhotoImage(file='images/pic-icon.png'))
        
        self.container = Frame(self)
        self.container.grid(row=0, column=0, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (login.LoginPage, register.RegisterPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(login.LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
