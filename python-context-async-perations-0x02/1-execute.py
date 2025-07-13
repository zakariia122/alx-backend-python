import sqlite3

class ExecuteQuery:
    def __init__(self, query, params=()):
        self.query = query
        self.params = params

    def __enter__(self):
        self.conn = sqlite3.connect('my_database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


if __name__ == "__main__":
    with ExecuteQuery("SELECT * FROM users WHERE age > ?", (25,)) as result:
        print(result)
