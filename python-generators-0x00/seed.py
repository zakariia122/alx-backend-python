import mysql.connector
import csv

def connect_db():
    print("Attempting to connect to MySQL server...")
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password" # Replace with your MySQL password
        )
        print("Connection successful!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created or already exists.")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")
    cursor.close()

def connect_to_prodev():
    print("Attempting to connect to ALX_prodev database...")
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="zakaria2004", # Replace with your MySQL password
            database="ALX_prodev"
        )
        print("Connected to ALX_prodev successfully!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id VARCHAR(255) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age INT NOT NULL
            )
        """)
        print("Table user_data created or already exists.")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
    cursor.close()

def insert_data(connection, csv_file_path):
    cursor = connection.cursor()
    try:
        with open(csv_file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                cursor.execute("SELECT user_id FROM user_data WHERE user_id = %s", (row[0],))
                if cursor.fetchone() is None: # Check if data already exists
                    sql = "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql, tuple(row))
        connection.commit()
        print("Data inserted successfully!")
    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")
    cursor.close()

