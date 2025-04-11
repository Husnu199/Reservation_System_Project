import tkinter as tk
from gui.login import LoginWindow
from database.db_manager import create_table, create_users_table

def main():
    create_table()

    root = tk.Tk()
    root.title("Restaurant Booking System")
    root.geometry("500x500")

    LoginWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    create_table()
    create_users_table()