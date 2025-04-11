import tkinter as tk
from tkinter import messagebox
from gui.main_menu import MainMenu  # Giriş başarılı olunca çağrılacak
from database.db_manager import get_connection


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack(pady=40)

        # Username and Password entry area
        tk.Label(self.frame, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Password:").grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1)

        # Login button
        self.login_button = tk.Button(self.frame, text="Log in", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=20)

        # Enter button support
        self.root.bind('<Return>', self.enter_pressed)

    def enter_pressed(self, event):
        self.login()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()

            if user:
                messagebox.showinfo("Success", "Login Successful")
                self.frame.destroy()
                MainMenu(self.root)
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")

        except Exception as e:
            messagebox.showerror("Error", f"Database error:\n{str(e)}")

        finally:
            conn.close()
