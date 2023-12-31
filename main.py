import tkinter as tk
from tkinter import messagebox
import sqlite3

# creat databas
conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# creat a table
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    firstname, lastname TEXT NOT NULL,
                    password TEXT NOT NULL)''')
conn.commit()

# creat a window
root = tk.Tk()
root.geometry("450x500")
root.title("Student Project")

# creat a label
label = tk.Label(root, text="Student Project", font=("Arial", 20))
def sign_page():
    def save_data():
        username = yourusername_entry.get()
        password = yourpasswords_entry.get()

        with open('user_data.txt', 'a') as f:
            f.write(f"{username},{password}\n")

        messagebox.showinfo("Success", "Registration successful.")

    sign_window = tk.Toplevel(root)
    sign_window.title("Register")

    yourusername_label = tk.Label(sign_window, text='Enter your username:')
    yourusername_label.pack()
    yourusername_entry = tk.Entry(sign_window)
    yourusername_entry.pack()

    yourpasswords_label = tk.Label(sign_window, text='Enter your password:')
    yourpasswords_label.pack()
    yourpasswords_entry = tk.Entry(sign_window, show='*')
    yourpasswords_entry.pack()

    save_button = tk.Button(sign_window, text="Save", command=save_data)
    save_button.pack()

# login
def login():
    username = yourusername_entry.get()
    password = yourpasswords_entry.get()

    with open('user_data.txt', 'r') as f:
        for line in f:
            stored_username, stored_password = line.strip().split(',')
            stored_firstname = stored_username.split()[0]
            if username == stored_username and password == stored_password:
                messagebox.showinfo("Success", f"Welcome,{stored_firstname}")
                return

    messagebox.showerror("Error", "Incorrect username or password.")

# search
def search():
    search_username = yourusername_entry.get()

    with open('user_data.txt', 'r') as f:
        for line in f:
            stored_username, stored_password = line.strip().split(',')
            if search_username == stored_username:
                messagebox.showinfo("Result", f"Username: {stored_username}\nPassword: {stored_password}")
                return

    messagebox.showinfo("Result", "User not found.")

# crear a sign button
sign_button = tk.Button(text="Sign Up", command=sign_page)
sign_button.pack()

# creat username and passwords
yourusername_label = tk.Label(root, text='Enter your username:')
yourusername_label.pack()
yourusername_entry = tk.Entry(root)
yourusername_entry.pack()

yourpasswords_label = tk.Label(root, text='Enter your password:')
yourpasswords_label.pack()
yourpasswords_entry = tk.Entry(root, show='*')
yourpasswords_entry.pack()

# creat login buttom
login_button = tk.Button(text="Login", command=login)
login_button.pack()

# creat search button
search_button = tk.Button(text="Search", command=search)
search_button.pack()

root.mainloop()