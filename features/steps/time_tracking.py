from behave import given, when, then
from pprint import pprint
import json

# Scenario: Add hours for task

@given(u'a task')
def step_impl(context):
    context.response = context.client.get("/task/1")
    context.response.json_task_before = json.loads(context.response.data)
    assert context.response.json_task_before["description"] == "Agregar ayuda que diga como agregar nuevo candidato"
    assert context.response.json_task_before["timeElapsed"] == 2

@when(u'one hour is added to the task')
def step_impl(context):
    response = context.client.post("/task/" + str(context.response.json_task_before["id"]), data=dict(hours=1))
    assert response.status_code == 200

@then(u'the count should increase by one')
def step_impl(context):
    response = context.client.get("/task/" + str(context.response.json_task_before["id"]))
    task = json.loads(response.data)
    assert task["timeElapsed"] == 3

# Scenario: Add hours to finished task

@given(u'a task with status done')
def step_impl(context):
    context.response = context.client.get("/task/0")
    context.response.json_task_before = json.loads(context.response.data)
    assert context.response.json_task_before["status"] == "done"
    assert context.response.json_task_before["timeElapsed"] == 5

@when(u'trying to add one hour to a finished task')
def step_impl(context):
    response = context.client.post("/task/" + str(context.response.json_task_before["id"]), data=dict(hours=1))
    assert response.status_code == 500

@then(u'the time should remain the same')
def step_impl(context):
    response = context.client.get("/task/" + str(context.response.json_task_before["id"]))
    task = json.loads(response.data)
    assert task["timeElapsed"] == context.response.json_task_before["timeElapsed"] 

# Scenario: Add hours to pending task

@given(u'a task with pending status')
def step_impl(context):
    context.response = context.client.get("/task/4")
    context.response.json_task_before = json.loads(context.response.data)
    assert context.response.json_task_before["status"] == "pending"
    assert context.response.json_task_before["timeElapsed"] == 0

@when(u'adding one hour')
def step_impl(context):
    response = context.client.post("/task/" + str(context.response.json_task_before["id"]), data=dict(hours=1))
    assert response.status_code == 200

@then(u'one hour should be added')
def step_impl(context):
    response = context.client.get("/task/" + str(context.response.json_task_before["id"]))
    task = json.loads(response.data)
    assert task["timeElapsed"] == 1

@then(u'status should change to started')
def step_impl(context):
    response = context.client.get("/task/" + str(context.response.json_task_before["id"]))
    task = json.loads(response.data)
    assert task["status"] == "started"

