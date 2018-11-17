from flask import Flask, json
from tasks import Tasks
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/tasks")
def return_tasks():
    tasks = Tasks()
    return json.jsonify(tasks.get())

if __name__ == "__main__":
    app.run(host='10.116.170.191', port=5353)
