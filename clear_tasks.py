import sqlite3

def clear_tasks():
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("DELETE FROM tasks")
    conn.commit()
    conn.close()

clear_tasks()