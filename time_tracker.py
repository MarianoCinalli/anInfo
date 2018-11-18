from flask import Flask, json, request
from tasks import Tasks
from user import User
from project import Project
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/tasks", defaults={'projectName': None, 'userName': None})
@app.route("/tasks/<string:userName>", defaults={'projectName': None})
@app.route("/tasks/<string:userName>/<string:projectName>")
def return_tasks(userName, projectName):
    tasks = Tasks()
    user = None
    project = None
    if userName:
        user = User(userName)
    if projectName:
        project = Project(projectName)
    return json.jsonify(tasks.get(user, project))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5353)

