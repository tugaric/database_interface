import sqlite3
from typing import Tuple, List
from database.SQL import SQL_QUERY

class myModel:
    path = "database/article.db"

    def __init__(self):
        self.conn = sqlite3.connect(myModel.path)
        self.cursor = self.conn.cursor()

    def get_from_db(self, component_query): 
        self.cursor.execute(component_query)
        return self.cursor.fetchall()
    
    def insert_new_article(self, number, plan, FK_class):
        statement = """Insert into article (number, plan, FK_class) values (?,?,?)"""
        self.cursor.execute(statement, ( number, plan, FK_class))
        self.conn.commit()
        print("New article added to db...")

    def insert_new_class(self, name, description):
        statement = """Insert or replace into class (name, description) values (?,?);"""
        self.cursor.execute(statement, (name, description))
        self.conn.commit()
        print("New class added to db...")