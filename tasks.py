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
                "assignedTo": "jorge.bolco"
            },
            {
                "id": 2,
                "description": "Agregar ayuda que diga como agregar nuevo candidato",
                "timeElapsed": 2,
                "timeEstimated": 5,
                "status": "started",
                "assignedTo": "jorge.bolco"
            },
            {
                "id": 3,
                "description": "Arreglar el bug que evita agregar candidatos",
                "timeElapsed": 0,
                "timeEstimated": 10,
                "status": "",
                "assignedTo": "jorge.bolco"
            },
            {
                "id": 4,
                "description": "Agregar importar desde PC",
                "timeElapsed": 0,
                "timeEstimated": 20,
                "status": "done",
                "assignedTo": "justo.vaja"
            }
        ]

    def get(self, user=None):
        tasks = []
        if user:
            userName = user.getName()
            tasks = [task for task in self.tasks if task['assignedTo'] == userName]
        else:
            tasks = self.tasks
        return tasks


