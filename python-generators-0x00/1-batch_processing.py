from seed import connect_to_prodev

def stream_users_in_batches(batch_size):
    offset = 0
    while True:
        connection = connect_to_prodev()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}")
        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        if not rows:
            break

        yield rows
        offset += batch_size

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user["age"] > 25:
                print(user)
