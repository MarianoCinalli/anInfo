from user import User
from project import Project

class Task:
    next_id = 0

    def __init__(self, description, timeElapsed, timeEstimated, status, assignedTo, project):
        self.id = Task.next_id
        Task.next_id += 1
        self.description = description
        self.timeElapsed = timeElapsed
        self.timeEstimated = timeEstimated
        self.status = status
        self.assignedTo = assignedTo
        self.project = project

    def isAssigned(self, user):
        return self.assignedTo.getName() == user.getName()

    def isForProject(self, project):
        return self.project.getName() == project.getName()

    def addHours(self, hours):
        self.timeElapsed += hours

    def getAsDict(self):
        return {
            "id": self.id,
            "description": self.description,
            "timeElapsed": self.timeElapsed,
            "timeEstimated": self.timeEstimated,
            "status": self.status,
            "assignedTo": self.assignedTo.getName(),
            "project": self.project.getName()
        }

