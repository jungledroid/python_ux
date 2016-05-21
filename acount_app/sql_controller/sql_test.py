#!/usr/local/bin/env python3
#-*- coding utf-8 -*-
import sqlite3
class SqliteContoller:
    def __init__(self):
        pass

    def queryAll(self):
        conn = sqlite3.connect("../private.sqlite3")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM count")
        values = cursor.fetchall()
        print(values)
        conn.close()
        return values

    def deleteAllData(self):
        conn = sqlite3.connect("../private.sqlite3")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM count")
        conn.commit()
        values = cursor.fetchall()
        print(values)
        conn.close()
