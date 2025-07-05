import mysql.connector
from seed import connect_to_prodev

def stream_users():
    connection = None
    cursor = None
    try:
        connection = connect_to_prodev()
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT user_id, name, email, age FROM user_data")
            for row in cursor:
                yield row
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    print("Streaming users...")
    for user in stream_users():
        print(user)
    print("Finished streaming users.")
