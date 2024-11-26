from flask import Flask
from flask_apscheduler import APScheduler
app= Flask(__name__)

# sched = APScheduler()

# def job1():
#     print('This runs every 5 am')

# if __name__ == '__main__':
#     # sched.add_job(id='job1', func =job1, trigger ='interval', seconds = 5)
#     sched.add_job(id='job1', func =job1, trigger ='cron',day_of_week='mon-sun' ,hour =5, minute =56)
#     sched.start()
#     app.run(debug=True, use_reloader=False)



from apscheduler.schedulers.background import BackgroundScheduler
import re
import pytz


# Initialize APScheduler
scheduler = BackgroundScheduler()
scheduler.start()  # Start 


def run_threading_tasks(x, y):
    answer = x*y
    print( f"{answer}")

@app.route('/', methods = ['GET'])
def home():
    x=1
    y=2
    
    scheduler.add_job(
        run_threading_tasks,
        trigger="interval",
        minutes=1,
        args=[x, y],
        id=f"task_for_user_{x}",
        replace_existing=True
    )
    
    return f"{x}+{y}"



@app.route('/new', methods = ['GET'])
def new():
    x=1
    y=2
    
    
    return f"{x}+{y}"


if __name__ == '__main__':
    app.run(debug=True)
