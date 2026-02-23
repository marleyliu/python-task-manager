import sqlite3
from datetime import datetime 


#task = []

def add_task(title, description, due_time):
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    

    #data.append((title, description, due_time))
    c.execute('''INSERT INTO tasks (title, description, due_time) VALUES (?, ?, ?)''', (title, description, due_time))

    conn.commit()
    conn.close()

title = input("Title:")
description = input("Description:")
due_time = input("Due time in YYYY-MM-DD HH:MM")

add_task(title, description, due_time)
print("Task added!")






