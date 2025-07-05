import mysql.connector
import csv
import os

def connect_db():
    print("Attempting to connect to MySQL server...")
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="zakaria2004"
        )
        print("Connection successful!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL server: {err}")
        return None

def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created or already exists.")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")
    finally:
        cursor.close()

def connect_to_prodev():
    print("Attempting to connect to ALX_prodev database...")
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="zakaria2004",
            database="ALX_prodev"
        )
        print("Connected to ALX_prodev successfully!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to ALX_prodev database: {err}")
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
    finally:
        cursor.close()

def insert_data(connection, csv_file_path):
    cursor = connection.cursor()
    try:
        if not os.path.exists(csv_file_path):
            print(f"Error: CSV file not found at {csv_file_path}")
            return

        with open(csv_file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                cursor.execute("SELECT user_id FROM user_data WHERE user_id = %s", (row[0],))
                if cursor.fetchone() is None:
                    sql = "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql, tuple(row))
        connection.commit()
        print("Data inserted successfully!")
    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cursor.close()

if __name__ == "__main__":
    main_connection = connect_db()
    if main_connection is None:
        print("Failed to connect to MySQL server. Exiting.")
    else:
        try:
            create_database(main_connection)
            main_connection.close()

            prodev_connection = connect_to_prodev()
            if prodev_connection is None:
                print("Failed to connect to ALX_prodev database. Exiting.")
            else:
                try:
                    create_table(prodev_connection)
                    csv_file = "user_data.csv"
                    insert_data(prodev_connection, csv_file)
                finally:
                    prodev_connection.close()
        finally:
            if main_connection.is_connected():
                main_connection.close()
