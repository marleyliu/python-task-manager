import sqlite3

conn = sqlite3.connect("tasks.db")

c = conn.cursor()
c.execute( 
"""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    due_time TEXT 

) """
)

conn.commit()
conn.close()

def get_all_tasks():
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    all_tasks = []
    pulled_data = c.execute("SELECT * FROM tasks")
    for row in pulled_data:
        all_tasks.append(row)
    conn.close()
    return all_tasks

print(get_all_tasks())

