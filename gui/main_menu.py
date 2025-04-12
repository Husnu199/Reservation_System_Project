import tkinter as tk
from tkinter import messagebox
from gui.new_customer import NewCustomerWindow
from gui.reservation_window import ReservationWindow
from gui.reservation_list import ReservationListWindow  
from tkcalendar import DateEntry
from gui.customer_list import CustomerListWindow


class MainMenu:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack(pady=40)

        tk.Label(self.frame, text="Welcome!", font=("Arial", 16)).pack(pady=10)

        # add customer button
        tk.Button(self.frame, text="Add New Customer", command=self.add_customer).pack(pady=5)

        # add reservation button
        tk.Button(self.frame, text="Make a Reservation", command=self.open_reservation_window).pack(pady=5)

        # list reservation button
        tk.Button(self.frame, text="Show All Reservations", command=lambda: ReservationListWindow(self.root)).pack(pady=5)


        # list customer button
        tk.Button(self.frame, text="Show Customer List", command=self.open_customer_list).pack(pady=5)

    def add_customer(self):
        NewCustomerWindow(self.root)

    def open_reservation_window(self):
        ReservationWindow(self.root)

    def open_res_list(self):
        ReservationListWindow(self.root)

    def open_customer_list(self):
        CustomerListWindow(self.root)
