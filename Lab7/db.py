import os.path
import sqlite3


class DataBase:
    db = 'db.py'
    table = 'table.sql'

    def __init__(self, create_table = False):
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

    def __del__(self):
        self.__db.close()