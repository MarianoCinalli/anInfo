from flask import Flask, json, request, abort, render_template
from task import Task
from tasks import Tasks
from user import User
from project import Project

app = Flask(__name__)
tasksDao = Tasks()

app.template_folder = "./frontend/templates/"
app.static_folder = "./frontend/static/"

@app.route("/")
def time_tracker():
    return render_template('time_tracker.html')

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
    response = {}
    if request.method == 'POST':
        hours = json.loads(request.data)["hours"]
        hours = int(hours)
        try:
             tasksDao.addHours(taskId, hours)
        except Exception,e:
             abort(500)
    else:
        task = tasksDao.getTask(taskId)
        if task:
            response = task.getAsDict()
    return json.jsonify(response)

if __name__ == "__main__":
    app.run(host='localhost', port=5353)
