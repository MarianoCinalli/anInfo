class Tasks:
    tasks = {}

    def __init__(self):
        self.tasks = [
            {
                "id": 1,
                "description": "Agregar icono con la imagen del usuario logeado",
                "timeElapsed": 5,
                "timeEstimated": 5,
                "status": "done",
                "assignedTo": "jorge.bolco",
                "project": "crm"
            },
            {
                "id": 2,
                "description": "Agregar ayuda que diga como agregar nuevo candidato",
                "timeElapsed": 2,
                "timeEstimated": 5,
                "status": "started",
                "assignedTo": "jorge.bolco",
                "project": "crm"
            },
            {
                "id": 3,
                "description": "Arreglar el bug que evita agregar candidatos",
                "timeElapsed": 0,
                "timeEstimated": 10,
                "status": "pending",
                "assignedTo": "jorge.bolco",
                "project": "crm"
            },
            {
                "id": 4,
                "description": "Agregar importar desde PC",
                "timeElapsed": 0,
                "timeEstimated": 20,
                "status": "started",
                "assignedTo": "justo.vaja",
                "project": "crm"
            },
            {
                "id": 5,
                "description": "Agregar barra de tareas",
                "timeElapsed": 0,
                "timeEstimated": 30,
                "status": "pending",
                "assignedTo": "jorge.bolco",
                "project": "business.analytics"
            }
        ]

    def get(self, user=None, project=None):
        tasks = []
        if user and project:
            userName = user.getName()
            projectName = project.getName()
            tasks = [task for task in self.tasks if task['assignedTo'] == userName and task['project'] == projectName]
        elif user and not project:
            userName = user.getName()
            tasks = [task for task in self.tasks if task['assignedTo'] == userName]
        else:
            tasks = self.tasks
        return tasks


