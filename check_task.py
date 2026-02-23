import time
import schedule
from database import get_all_tasks
from datetime import datetime 
from notification import send_notification


def check_tasks():
    time = datetime.now().strftime("%Y-%m-%d %H:%M")
    all_tasks = get_all_tasks()
    for task in all_tasks: 
        if time == task[3]:
            send_notification(task[1], "Due now!")
schedule.every(10).seconds.do(check_tasks)

while True:
    schedule.run_pending()
    time.sleep(1)

