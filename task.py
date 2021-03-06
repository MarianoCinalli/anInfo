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
        if hours < 0:
            raise Exception("Can't add negative hours")
        if self.status == "done":
            raise Exception("Can't increase the time elapsed for a task with status 'done'")
        if self.assignedTo.getMaxHours() < hours:
            raise Exception("Can't assign more hours that the user is allowed.")
        if self.status == "pending":
            self.status = "started"
        self.timeElapsed += hours

    def finish(self):
        self.status = "done"

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
