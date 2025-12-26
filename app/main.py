import argparse
from app.database.db import SessionLocal
from repositories.task import TaskRepository
from repositories.focus_session import FocusSessionRepository
from datetime import datetime


class Service:
    def __init__(self):
        self.session = SessionLocal

    def create_task(self, name):
        with self.session() as session:
            task = TaskRepository.create(session, name)
        return task
    def all_task(self):
        with self.session() as session:
            tasks = TaskRepository.get_all(session)
        return tasks
    def start_focus_in_task(self, task_id, duration: int = 0):
        with self.session() as session:
            focus_session = FocusSessionRepository.create(session, task_id, duration)
        return focus_session
    def finish_focus_in_task(self, task_id, end_time: datetime = datetime.now()):
        with self.session() as session:
            focus_session = FocusSessionRepository.update(session, task_id, end_time=end_time)
            TaskRepository.update(session, task_id, focus_session.duration)
        return focus_session
    def total_time_in_task(self, task_id):
        with self.session() as session:
            total_time = FocusSessionRepository.get_total_duration_for_task(session, task_id)
        return total_time
    
class App:
    def __init__(self) -> None:
        self.service = Service()

    def create_task(self, name):
        task = self.service.create_task(name)
        return f"Задача ID: {task.id}\nName: {task.name}"
    def start_focus_in_task(self, task_id, duration: int = 0):
        focus_session = self.service.start_focus_in_task(task_id, duration)
        if duration == 0:
            return f"Бесконечная рабочая сессия запущена"
        time_type = ''
        if duration > 60:
            duration=round(duration / 60)
            time_type = 'часов'
        elif 0 < duration < 60:
            time_type = 'минут'
        return f"Рабочая сессия длинною в {duration} {time_type} стартовала"
    def finish_focus_in_task(self, task_id):
        focus_session = self.service.finish_focus_in_task(task_id)
        return f"Рабочая сессия завершена общее время в задаче {round(focus_session.duration/60)} минут"
    
    def get_all_tasks(self):
        tasks = self.service.all_task()
        for task in tasks:
            print(f"\nID: {task.id}\nНазвание: {task.name}\nОбщее время: {round(task.time_spent/60)} ч.\n")
    


while True:
    print("Timer App\n")
    app = App()
    print("Все задачи - all\nСоздать новую - create\nЗапустить таймер - start id work_time\nЗакончить - stop")

