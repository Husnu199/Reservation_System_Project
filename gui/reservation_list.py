import tkinter as tk
from tkinter import ttk, messagebox
from database.db_manager import get_connection

class ReservationListWindow:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("All Reservations")

        self.tree = ttk.Treeview(
            self.window,
            columns=("ID", "Name", "Table", "Party", "Date", "Time"),
            show="headings"
        )

        # Başlıklar
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Customer Name")
        self.tree.heading("Table", text="Table No")
        self.tree.heading("Party", text="Party Size")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Time", text="Time")

        # Kolon genişlikleri (opsiyonel)
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Name", width=150)
        self.tree.column("Table", width=80, anchor="center")
        self.tree.column("Party", width=100, anchor="center")
        self.tree.column("Date", width=100, anchor="center")
        self.tree.column("Time", width=80, anchor="center")

        self.tree.pack(padx=10, pady=10)

        self.load_reservations()

        tk.Button(self.window, text="Delete Selected", command=self.delete_reservation).pack(pady=10)

    def load_reservations(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT reservation_id, reservation_name, reservation_table, party_size, reservation_date, reservation_time
                FROM Reservations
            """)
            rows = cursor.fetchall()

            for row in rows:
                self.tree.insert("", tk.END, values=row)

        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()

    def delete_reservation(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a reservation to delete.")
            return

        reservation_id = self.tree.item(selected_item[0])["values"][0]

        confirm = messagebox.askyesno("Confirm", f"Delete reservation ID {reservation_id}?")
        if not confirm:
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Reservations WHERE reservation_id = %s", (reservation_id,))
            conn.commit()
            messagebox.showinfo("Success", "Reservation deleted.")
            self.tree.delete(selected_item[0])

        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()
