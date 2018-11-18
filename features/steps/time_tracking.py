from behave import given, when, then
from pprint import pprint
import json

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

