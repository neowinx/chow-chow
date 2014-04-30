import sqlite3

con = sqlite3.connect("chow-chow.db")
con.isolation_level = None
cur = con.cursor()


def create_initial_schema():
    cur.executescript("""
        create table task(
          id REAL primary key,
          task TEXT,
          time INTEGER,
          start TIMESTAMP
        );
    """)


def insert_task_in_db(id_task,task, time, start):
    cur.execute("insert into task(id,task, time, start) values (?,?, ?, ?)", (id_task,task, time, start))


def insert_tasks_in_db(tasks):
    cur.executemany("insert into task(id, task, time, start) values (?, ?, ?, ?)", tasks)

def select_tasks_in_db():
    cur.execute("select * from task")
    return cur.fetchall()
    
