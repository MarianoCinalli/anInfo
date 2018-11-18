class User:
    name = ""
    hoursPerProyect = 80

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getMaxHours(self):
        return self.hoursPerProyect
