import os
import sqlite3
import pandas as pd
from pathlib import Path


cnct = sqlite3.connect('data.db', check_same_thread=False)

cnct.row_factory = sqlite3.Row

def sql_query(query):
    cur = cnct.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query,var):
    cur = cnct.cursor()
    cur.execute(query,var)
    cnct.commit()

def sql_delete(query,var):
    cur = cnct.cursor()
    cur.execute(query,var)

def sql_query2(query,var):
    cur = cnct.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows