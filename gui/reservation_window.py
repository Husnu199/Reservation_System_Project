import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from database.db_manager import get_connection



class ReservationWindow:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("New Reservation")

        tk.Label(self.window, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.window, text="Table No:").grid(row=1, column=0)
        self.table_entry = tk.Entry(self.window)
        self.table_entry.grid(row=1, column=1)

        tk.Label(self.window, text="Party Size:").grid(row=2, column=0)
        self.party_entry = tk.Entry(self.window)
        self.party_entry.grid(row=2, column=1)

        tk.Label(self.window, text="Date:").grid(row=3, column=0)
        self.date_entry = DateEntry(self.window)
        self.date_entry.grid(row=3, column=1)

        tk.Button(self.window, text="Save", command=self.save_reservation).grid(row=4, column=0, columnspan=2)

        self.window.bind('<Return>', self.enter_pressed)

    def enter_pressed(self, event):
        self.save_reservation()

    def save_reservation(self):
        name = self.name_entry.get()
        table_no = self.table_entry.get()
        party_size = self.party_entry.get()
        date = self.date_entry.get_date()

        if not name or not table_no or not party_size or not date:
            messagebox.showerror("Error", "Please fill all fields")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Control if user exist in db
            cursor.execute("SELECT customer_id FROM Customers WHERE customer_name = %s", (name,))
            result = cursor.fetchone()

            if not result:
                messagebox.showerror("Not Found", "Customer not registered. Please add them first.")
                return

            customer_id = result[0]

            # Connect reservation to customers table
            cursor.execute("""
                INSERT INTO Reservations (reservation_name, reservation_table, party_size, reservation_date, customer_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (name, table_no, party_size, date, customer_id))

            conn.commit()
            messagebox.showinfo("Success", "Reservation saved successfully.")
            self.window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Database error:\n{str(e)}")

        finally:
            conn.close()

