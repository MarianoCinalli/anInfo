from behave import given, then
import json
from pprint import pprint

@given(u'a user requets all tasks')
def step_impl(context):
    context.response = context.client.get('/tasks')
    context.response.json_data = json.loads(context.response.data)
    assert len(context.response.json_data) == 1

@then(u'the user sees all tasks')
def step_impl(context):
    assert context.response.json_data[0]['description'] == 'Agregar icono con la imagen del usuario logeado'
