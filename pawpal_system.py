from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional

@dataclass
class Task:
    description: str
    time: str
    duration_minutes: int
    priority: str
    frequency: str
    completed: bool = False
    due_date: Optional[date] = None

    def mark_complete(self):
        pass

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        pass

    def get_tasks(self) -> List[Task]:
        pass

class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        pass

    def get_all_tasks(self) -> List[Task]:
        pass

class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def sort_by_time(self) -> List[Task]:
        pass

    def filter_tasks(self, pet_name: str = None, status: bool = None) -> List[Task]:
        pass

    def detect_conflicts(self) -> List[str]:
        pass

    def handle_recurrence(self, task: Task):
        pass