from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.state('zoomed')
window.resizable(0, 0)
window.geometry("400x400")
window.minsize(750, 650) 
window.maxsize(750, 650)
window.title('Monja Uploader')

# icon photo
icon = PhotoImage(file='images\\pic-icon.png')
window.iconphoto(True, icon)

LoginPage = Frame(window)

window.mainloop()
