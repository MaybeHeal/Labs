import os.path
import sqlite3


class DataBase:
    db = 'db.db'
    table = 'table.sql'

    def __init__(self, create_table=False):
        if not os.path.exists(self.db):
            create_table = True
        self.__db = sqlite3.connect(self.db)
        self.__db.row_factory = sqlite3.Row
        self.__cur = self.__db.cursor()
        if create_table:
            self.create_table()

    def create_table(self):
        with open(self.table, 'r') as data_base:
            self.__cur.executescript(data_base.read())
        self.__db.commit()

    def add_item(self, table, columns, values):
        try:
            self.__cur.execute(f'INSERT INTO {table} {columns} VALUES {values}')
            self.__db.commit()
            return self.__cur.lastrowid
        except sqlite3.Error as e:
            print('Ошибка записи в БД:', e)
            return None

    def update_item(self, table, item_id, column, value):
        try:
            self.__cur.execute(f'UPDATE {table} SET {column}={value} WHERE id={item_id}')
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка обновления данных в БД:', e)

    def get_item(self, table, item_id):
        try:
            self.__cur.execute(f'SELECT * FROM {table} WHERE id={item_id}')
            return self.__cur.fetchone()
        except sqlite3.Error as e:
            print('Ошибка чтения БД:', e)
            return None

    def get_item_count(self, table, column, value):
        try:
            self.__cur.execute(f'SELECT count(id) FROM {table} WHERE {column}={value}')
            return self.__cur.fetchone()[0]
        except sqlite3.Error as e:
            print('Ошибка чтения БД:', e)
            return None

    def get_all_items(self, table):
        try:
            self.__cur.execute(f'SELECT * FROM {table}')
            return self.__cur.fetchall()
        except sqlite3.Error as e:
            print('Ошибка чтения БД:', e)
            return None

    def clear_table(self, table):
        try:
            self.__cur.execute(f'DELETE FROM {table}')
            self.__cur.execute(f'DELETE FROM sqlite_sequence where name="{table}"')
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка удаления из БД:', e)

    def __del__(self):
        self.__db.close()


if __name__ == '__main__':
    db = DataBase()
    db.clear_table('employee')
    db.clear_table('edition')
    db.clear_table('department')
