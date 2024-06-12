import tkinter as tk
from tkinter import messagebox

# Function to handle login
def login():
    username = "johnsmith"
    password = "12345"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        open_dashboard()
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

# Function to handle forgot password
def forgot_password():
    messagebox.showinfo(title="Forgot Password", message="Please contact support to reset your password.")

# Function to handle registration
def register():
    register_window = tk.Toplevel(window)
    register_window.title("Register")
    register_window.geometry('340x440')
    register_window.configure(bg='#444444')

    # Registration form widgets
    register_label = tk.Label(register_window, text="Register", bg='#444444', fg="#FF3399", font=("Arial", 30))
    new_username_label = tk.Label(register_window, text="New Username", bg='#444444', fg="#FFFFFF", font=("Arial", 16))
    new_username_entry = tk.Entry(register_window, font=("Arial", 16))
    new_password_label = tk.Label(register_window, text="New Password", bg='#444444', fg="#FFFFFF", font=("Arial", 16))
    new_password_entry = tk.Entry(register_window, show="*", font=("Arial", 16))
    register_button = tk.Button(register_window, text="Register", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16),
                                command=lambda: messagebox.showinfo(title="Register", message="Registration is currently unavailable."))

    # Placing widgets on the screen
    register_label.pack(pady=40)
    new_username_label.pack()
    new_username_entry.pack(pady=10)
    new_password_label.pack()
    new_password_entry.pack(pady=10)
    register_button.pack(pady=30)

# Function to open the dashboard
def open_dashboard():
    dashboard = tk.Toplevel(window)
    dashboard.title("Dashboard")
    dashboard.geometry('340x440')
    dashboard.configure(bg='#333333')
    welcome_label = tk.Label(dashboard, text="Welcome to the Dashboard", bg='#333333', fg="#FF3399", font=("Arial", 20))
    welcome_label.pack(pady=20)

# Create the main application window
window = tk.Tk()
window.title("Login Form")
window.geometry('360x480')
window.configure(bg='#444444')

# Create a frame for the login form
frame = tk.Frame(bg='#444444')

# Creating widgets for the login form
login_label = tk.Label(frame, text="Login", bg='#444444', fg="#FF3399", font=("Arial", 30))
username_label = tk.Label(frame, text="Username", bg='#444444', fg="#FFFFFF", font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 16))
password_label = tk.Label(frame, text="Password", bg='#444444', fg="#FFFFFF", font=("Arial", 16))
password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
login_button = tk.Button(frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)
forgot_password_button = tk.Button(frame, text="Forgot Password", bg="#FF3399", fg="#FFFFFF", font=("Arial", 12), command=forgot_password)
register_button = tk.Button(frame, text="Register", bg="#FF3399", fg="#FFFFFF", font=("Arial", 12), command=register)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
forgot_password_button.grid(row=4, column=0, columnspan=2, pady=10)
register_button.grid(row=5, column=0, columnspan=2, pady=10)

frame.pack(pady=50)

window.mainloop()
