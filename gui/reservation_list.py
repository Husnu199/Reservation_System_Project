import tkinter as tk
from tkinter import ttk
from database.db_manager import get_connection

class ReservationListWindow:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("All Reservations")

        # Treeview
        columns = ("ID", "Name", "Table", "Party Size", "Date")
        self.tree = ttk.Treeview(self.window, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        self.tree.pack(padx=10, pady=10)

        self.load_reservations()

    def load_reservations(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT reservation_id, reservation_name, reservation_table, party_size, reservation_date FROM Reservations")
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=row)

        connection.close()
