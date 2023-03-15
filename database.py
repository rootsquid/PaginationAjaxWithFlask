import sqlite3
import json

class Database:


    def __init__(self, db_name: str = 'database.db') -> None:
        with sqlite3.connect(db_name) as self.conn:
            self.db_name = db_name
            self.cursor = self.conn.cursor()
            self.create_table()

        
    def create_table(self) -> None:
        with sqlite3.connect(self.db_name) as self.conn:
            self.cursor = self.conn.cursor()
            self.cursor.execute('CREATE TABLE IF NOT EXISTS random_table (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
            self.conn.commit()


    def insert_data(self, name: str, age: int) -> None:
        with sqlite3.connect(self.db_name) as self.conn:
            self.cursor = self.conn.cursor()
            self.cursor.execute('INSERT INTO random_table (name, age) VALUES (?, ?)', (name, age))
            self.conn.commit()


    def isEmpty(self) -> bool:
        with sqlite3.connect(self.db_name) as self.conn:
            self.cursor.execute('SELECT * FROM random_table')
            if self.cursor.fetchall():
                return False
            else:
                return True


    def get_all_data(self) -> str:
        with sqlite3.connect(self.db_name) as self.conn:
            self.cursor = self.conn.cursor()
            self.cursor.execute('SELECT id, name, age FROM random_table')
            data = self.cursor.fetchall()
            return list(data)


    def get_data(self, page: int) -> str:
        with sqlite3.connect(self.db_name) as self.conn:
            page = int(page) * 5
            self.cursor = self.conn.cursor()
            self.cursor.execute('SELECT id, name, age FROM random_table LIMIT 5 OFFSET ?', (page,))
            data = self.cursor.fetchall()
            return list(data)

    
    def get_total_rows(self) -> int:
        with sqlite3.connect(self.db_name) as self.conn:
            self.cursor = self.conn.cursor()
            self.cursor.execute('SELECT * FROM random_table')
            return len(self.cursor.fetchall())

