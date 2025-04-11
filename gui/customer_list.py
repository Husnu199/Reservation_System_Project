import tkinter as tk
from tkinter import ttk, messagebox
from database.db_manager import get_connection

class CustomerListWindow:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Customer List")

        columns = ("ID", "Name", "Phone", "Email")
        self.tree = ttk.Treeview(self.window, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        self.tree.pack(padx=10, pady=10)

        # Sil butonu
        tk.Button(self.window, text="Delete Selected Customer", command=self.delete_customer).pack(pady=5)

        self.load_customers()

    def load_customers(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT customer_id, customer_name, customer_phone_number, customer_address FROM Customers")
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=row)
        conn.close()

    def delete_customer(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a customer to delete.")
            return

        customer_id = self.tree.item(selected[0])["values"][0]

        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete customer ID {customer_id}?")
        if not confirm:
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Customers WHERE customer_id = %s", (customer_id,))
            conn.commit()
            conn.close()

            self.tree.delete(selected[0])
            messagebox.showinfo("Success", "Customer deleted successfully.")

        except Exception as e:
            messagebox.showerror("Error", f"Database error:\n{str(e)}")
