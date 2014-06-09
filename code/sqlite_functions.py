import sqlite3
import os

con = sqlite3.connect("chow-chow.db")
con.isolation_level = None
cur = con.cursor()


def db_create_initial_schema():
    rows = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='task'").fetchall()
    if len(rows) <= 0:
        cur.executescript("""
            create table task(
              id REAL primary key,
              task TEXT,
              time INTEGER,
              start TIMESTAMP
            );
        """)


def db_insert_task(id_task, task, time, start):
    cur.execute("insert into task(id,task, time, start) values (?,?, ?, ?)", (id_task, task, time, start))


def db_insert_tasks(tasks):
    cur.executemany("insert into task(id, task, time, start) values (?, ?, ?, ?)", tasks)


def db_select_tasks():
    cur.execute("select * from task")
    return cur.fetchall()


def db_delete_tasks():
    return cur.execute("delete from task").rowcount