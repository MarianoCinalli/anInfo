class Tasks:
    def get(self):
        tasks = [ 
            {
                "id": 1,
                "description": "Agregar icono con la imagen del usuario logeado",
                "timeElapsed": 10,
                "timeEstimated": 12,
                "status": "done"
            }
        ]
        return tasks

