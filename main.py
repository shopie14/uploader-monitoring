import tkinter as tk
from tkinter import messagebox, PhotoImage
from PIL import ImageTk, Image

# Importing functions from your src.form module
from src import login, register

# Initialize the main window
window = tk.Tk()
window.title("Monja Uploader")
window.geometry('660x680')
window.configure(bg='#83B4FF')
frame = tk.Frame(window, bg='#83B4FF')
icon = PhotoImage(file='images\\pic-icon.png')
window.iconphoto(True, icon)

def navigasi():
    nav = tk.Label(frame, text='Monja Uploader', bg='#FDFFE2', fg='#83B4FF', font=('Poppins', 28, 'bold'))
    nav.pack(pady=130)  

def btn_navigasi():
    # Create Login button
    btn_login = tk.Button(frame, text='Login', bg='#005C78',  fg="#FFFFFF", font=("Poppins", 16), command=login.show_login_form)
    btn_login.config(borderwidth=0, border=0, width=20, pady=5, relief=tk.RIDGE)  # Set same size and round corners
    btn_login.pack(pady=20, padx=100) # Add top padding

    # Create Register button
    register_button = tk.Button(frame, text="Register", bg="#005C78", fg="#FFFFFF", font=("Poppins", 16), command=register)
    register_button.config(borderwidth=0, border=0, width=20, pady=5, relief=tk.RIDGE)  # Set same size and round corners
    register_button.pack(pady=10, padx=20)  # Add some padding between the buttons

# Call the navigasi function to add the label to the frame
navigasi()

btn_navigasi()  # Call the button function to add buttons

frame.pack(padx=30, pady=30)
window.mainloop()
