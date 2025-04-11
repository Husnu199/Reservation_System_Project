import tkinter as tk
from tkinter import messagebox
from database.db_manager import get_connection

class NewCustomerWindow:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Add New Customer")

        tk.Label(self.window, text="Full Name: ").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.window, text="Mail Address: ").grid(row=1, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(self.window)
        self.address_entry.grid(row=1, column=1)

        tk.Label(self.window, text="Phone Number: ").grid(row=2, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(self.window)
        self.phone_entry.grid(row=2, column=1)

        tk.Button(self.window, text="Save", command=self.save_customer).grid(row=3, column=0, columnspan=2, pady=10)

        self.window.bind('<Return>', self.enter_pressed)

    def enter_pressed(self, event):
        self.save_customer()

    def save_customer(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        phone = self.phone_entry.get()

        if not name or not address or not phone:
            messagebox.showerror("Error", "Please fill all fields")
            return

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Customers WHERE customer_phone_number = %s", (phone,))
            if cursor.fetchone():
                messagebox.showerror("Error", "This phone number is already registered.")
                return

            cursor.execute("""
                INSERT INTO Customers (customer_name, customer_address, customer_phone_number)
                VALUES (%s, %s, %s)
            """, (name, address, phone))

            connection.commit()
            messagebox.showinfo("Success", "Customer registered successfully.")
            self.window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Database error:\n{str(e)}")
        finally:
            connection.close()
