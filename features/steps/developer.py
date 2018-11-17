from behave import given, then
import json

user="jorge.bolco"

@given(u'a user requets all tasks')
def step_impl(context):
    context.response = context.client.get('/tasks')
    # Lo que se seteo aca va a pasar al context del siguiente step del test.
    context.response.json_data = json.loads(context.response.data)
    assert len(context.response.json_data) == 4

@then(u'the user sees all tasks')
def step_impl(context):
    assert context.response.json_data[0]['description'] == 'Agregar icono con la imagen del usuario logeado'
    assert context.response.json_data[1]['description'] == 'Agregar ayuda que diga como agregar nuevo candidato'
    assert context.response.json_data[2]['description'] == 'Arreglar el bug que evita agregar candidatos'
    assert context.response.json_data[3]['description'] == 'Agregar importar desde PC'

@given(u'{user} requets his tasks')
def step_impl(context, loggedUser):
    context.response = context.client.get('/tasks', data=dict(user=loggedUser))
    context.response.json_data = json.loads(context.response.data)
    assert len(context.response.json_data) == 3

@then(u'{user} sees his tasks')
def step_impl(context):
    assert context.response.json_data[0]['description'] == 'Agregar icono con la imagen del usuario logeado'
    assert context.response.json_data[1]['description'] == 'Agregar ayuda que diga como agregar nuevo candidato'
    assert context.response.json_data[2]['description'] == 'Arreglar el bug que evita agregar candidatos'

