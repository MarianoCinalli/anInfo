from behave import given, then
import json

user="jorge.bolco"

@given(u'a user requests all tasks')
def step_impl(context):
    context.response = context.client.get('/tasks')
    # Lo que se seteo aca va a pasar al context del siguiente step del test.
    context.response.json_data = json.loads(context.response.data)
    assert len(context.response.json_data) == 5

@then(u'the user sees all tasks')
def step_impl(context):
    assert context.response.json_data[0]['description'] == 'Agregar icono con la imagen del usuario logeado'
    assert context.response.json_data[1]['description'] == 'Agregar ayuda que diga como agregar nuevo candidato'
    assert context.response.json_data[2]['description'] == 'Arreglar el bug que evita agregar candidatos'
    assert context.response.json_data[3]['description'] == 'Agregar importar desde PC'
    assert context.response.json_data[4]['description'] == 'Agregar barra de tareas'

@given(u'{user} requests his tasks')
def step_impl(context, user):
    context.response = context.client.get("/tasks/" + user)
    context.response.json_data = json.loads(context.response.data)
    assert len(context.response.json_data) == 4

@then(u'jorge.bolco sees his tasks')
def step_impl(context):
    assert context.response.json_data[0]['description'] == 'Agregar icono con la imagen del usuario logeado'
    assert context.response.json_data[1]['description'] == 'Agregar ayuda que diga como agregar nuevo candidato'
    assert context.response.json_data[2]['description'] == 'Arreglar el bug que evita agregar candidatos'
    assert context.response.json_data[3]['description'] == 'Agregar barra de tareas'


@given(u'{user} requests his tasks for the {project} project')
def step_impl(context, user, project):
    context.response = context.client.get("/tasks/" + project + "/" + user)
    context.response.json_data = json.loads(context.response.data)
    assert len(context.response.json_data) == 3

@then(u'jorge.bolco sees his tasks for the crm project')
def step_impl(context):
    assert context.response.json_data[0]['description'] == 'Agregar icono con la imagen del usuario logeado'
    assert context.response.json_data[1]['description'] == 'Agregar ayuda que diga como agregar nuevo candidato'
    assert context.response.json_data[2]['description'] == 'Arreglar el bug que evita agregar candidatos'
