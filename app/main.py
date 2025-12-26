import argparse
from app.database.db import create_session
from repositories import focus_session, task


class ParseToCLI():
    pass

class Application:
    def __init__(self) -> None:
        self.session = create_session()

    def create_task(self):
        name = input("Name of this task: ")
        if 1 < len(name) < 200:
            new_task = task.TaskRepository.create(self.session, name)


while True:
    pass
    
