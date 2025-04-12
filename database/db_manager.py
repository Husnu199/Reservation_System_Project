import mysql.connector

# Get database connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Your Password should be here
        database="reservation_system"
    )

# Create tables
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    # Create customer tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customers (
            customer_id INT AUTO_INCREMENT PRIMARY KEY,
            customer_name VARCHAR(100) NOT NULL,
            customer_address VARCHAR(200) NOT NULL,
            customer_phone_number VARCHAR(20) UNIQUE NOT NULL
        )
    """)

    # Create reservation tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Reservations (
            reservation_id INT AUTO_INCREMENT PRIMARY KEY,
            reservation_name VARCHAR(100) NOT NULL,
            reservation_table INT,
            party_size INT,
            reservation_date DATE,
            customer_id INT,
            FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()

# add Reservation
def insert_reservation(name, table, party_size, date):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Reservations (reservation_name, reservation_table, party_size, reservation_date)
            VALUES (%s, %s, %s, %s)
        """, (name, table, party_size, date))

        conn.commit()

    except mysql.connector.Error as e:
        raise e

    finally:
        conn.close()

# Create user table and add admin user
def create_users_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL
        )
    """)

    cursor.execute("SELECT * FROM Users WHERE username = %s", ("admin",))
    if not cursor.fetchone():
        cursor.execute("INSERT INTO Users (username, password) VALUES (%s, %s)", ("admin", "1234"))

    conn.commit()
    conn.close()

