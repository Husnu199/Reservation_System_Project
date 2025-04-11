# 🍽️ Restaurant Booking System

A real-world restaurant reservation management system built with **Python (Tkinter)** and **MySQL**.

---

## 🚀 What Makes This Project Unique?

This project was originally intended to be built with **SQLite**, but was **migrated entirely to MySQL** to resemble a real-world production environment.

> ✅ Every module was written and understood by the developer  
> ✅ Strong grasp of GUI design, database integration, and user flows

---

## 🛠️ Technologies Used

- Python 3.13
- Tkinter (GUI)
- MySQL (via `mysql-connector-python`)
- OOP & modular architecture
- Git & GitHub for version control

---

## ✨ Features

### 🔐 Login System
- Admin login with real DB check (not hardcoded)
- Credentials are checked from `Users` table

### 👤 Add Customer
- Inputs: name, email, phone number
- Saved to `Customers` table with validation
- Duplicate phone check

### 📅 Make a Reservation
- Only allows reservations for registered customers
- Inputs: customer name, table number, party size, date
- Saved to `Reservations` table, linked via `customer_id`

### 📋 View & Manage Data
- List all customers
- List all reservations
- Delete any customer directly from the UI
- TreeView-based GUI for easy review

### ⌨️ Keyboard Shortcuts
- Pressing **Enter** submits forms (login, customer, reservation)

---

## 🔗 Project Structure

