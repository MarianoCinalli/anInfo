from flask import Flask, json, request
from task import Task
from tasks import Tasks
from user import User
from project import Project

app = Flask(__name__)
tasksDao = Tasks()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/tasks", defaults={'projectName': None, 'userName': None})
@app.route("/tasks/<string:userName>", defaults={'projectName': None})
@app.route("/tasks/<string:userName>/<string:projectName>")
def return_tasks(userName, projectName):
    user = None
    project = None
    if userName:
        user = User(userName)
    if projectName:
        project = Project(projectName)
    tasks = tasksDao.get(user, project)
    tasksDict = [task.getAsDict() for task in tasks]
    return json.jsonify(tasksDict)

@app.route("/task/<int:taskId>", methods=['GET', 'POST'])
def task(taskId):
    responce = {} 
    if request.method == 'POST':
        hours = int(request.values.get('hours'))
        try:
            tasksDao.addHours(taskId, hours)
        except Exception,e:
            abort(500)
    else:
        task = tasksDao.getTask(taskId)
        if task:
            responce = task.getAsDict()
    return json.jsonify(responce)

if __name__ == "__main__":
    app.run(host='10.116.170.191', port=5353)

