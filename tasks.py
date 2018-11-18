from task import Task
from user import User
from project import Project

class Tasks:
    def __init__(self):
        jorgeBolco = User("jorge.bolco")
        justoVaja = User("justo.vaja")
        crm = Project("crm")
        buisnesAnalytics = Project("business.analytics") 
        self.tasks = [
            Task (
                description = "Agregar icono con la imagen del usuario logeado",
                timeElapsed = 5,
                timeEstimated = 5,
                status = "done",
                assignedTo = jorgeBolco,
                project = crm
            ),
            Task (
                description = "Agregar ayuda que diga como agregar nuevo candidato",
                timeElapsed = 2,
                timeEstimated = 5,
                status = "started",
                assignedTo = jorgeBolco,
                project = crm
            ),
            Task (
                description = "Arreglar el bug que evita agregar candidatos",
                timeElapsed = 0,
                timeEstimated = 10,
                status = "pending",
                assignedTo = jorgeBolco,
                project = crm
            ),
            Task (
                description = "Agregar importar desde PC",
                timeElapsed = 0,
                timeEstimated = 20,
                status = "started",
                assignedTo = justoVaja,
                project = crm
            ),
            Task (
                description = "Agregar barra de tareas",
                timeElapsed = 0,
                timeEstimated = 30,
                status = "pending",
                assignedTo = jorgeBolco,
                project = buisnesAnalytics
            )
        ]
    
    
    def get(self, user=None, project=None):
        tasks = []
        if user and project:
            userName = user.getName()
            projectName = project.getName()
            tasks = [task for task in self.tasks if task.assignedTo.getName() == userName and task.project.getName() == projectName]
        elif user and not project:
            userName = user.getName()
            tasks = [task for task in self.tasks if task.assignedTo.getName() == userName]
        else:
            tasks = self.tasks
        return tasks

    def getTask(self, taskId):
        taskToReturn = None
        for task in self.tasks:
            if task.id == taskId:
                taskToReturn = task
        return taskToReturn

    def addHours(self, taskId, amount):
        for task in self.tasks:
            if task.id == taskId:
                task.addHours(amount)

