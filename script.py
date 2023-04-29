import tkinter as tk


def submit():
    username = username_entry.get()
    password = password_entry.get()
    print("Username: " + username)
    print("Password: " + password)
    # Add your code to validate the credentials here

root = tk.Tk()
root.title("Login Form")

username_label = tk.Label(root, text="Username")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()
