from flask import Flask, json, request
from tasks import Tasks
from user import User
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/tasks", defaults={'userName': None})
@app.route("/tasks/<string:userName>")
def return_tasks(userName):
    tasks = Tasks()
    user = None
    if userName:
        user = User(userName)
    return json.jsonify(tasks.get(user))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5353)

