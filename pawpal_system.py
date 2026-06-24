from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List, Optional

@dataclass
class Task:
    """Represents a single pet care activity."""
    description: str
    time: str
    duration_minutes: int
    priority: str
    frequency: str
    completed: bool = False
    due_date: Optional[date] = None

    def mark_complete(self):
        """Mark this task as complete."""
        self.completed = True

@dataclass
class Pet:
    """Represents a pet with a list of care tasks."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return this pet's list of tasks."""
        return self.tasks

class Owner:
    """Represents the pet owner who manages multiple pets."""
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to the owner's list."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks

class Scheduler:
    """The brain that organizes and manages tasks across all pets."""
    def __init__(self, owner: Owner):
        self.owner = owner

    def sort_by_time(self) -> List[Task]:
        """Return all tasks sorted by time in HH:MM format."""
        all_tasks = self.owner.get_all_tasks()
        return sorted(all_tasks, key=lambda t: t.time)

    def filter_tasks(self, pet_name: str = None, status: bool = None) -> List[Task]:
        """Filter tasks by pet name or completion status."""
        results = []
        for pet in self.owner.pets:
            for task in pet.get_tasks():
                if pet_name and pet.name != pet_name:
                    continue
                if status is not None and task.completed != status:
                    continue
                results.append(task)
        return results

    def detect_conflicts(self) -> List[str]:
        """Return warning messages for tasks scheduled at the same time."""
        all_tasks = self.owner.get_all_tasks()
        seen_times = {}
        warnings = []
        for task in all_tasks:
            if task.time in seen_times:
                warnings.append(
                    f"Conflict at {task.time}: '{seen_times[task.time]}' and '{task.description}'"
                )
            else:
                seen_times[task.time] = task.description
        return warnings

    def handle_recurrence(self, task: Task):
        """Create a new task for the next occurrence if the task is recurring."""
        if task.frequency == "daily":
            task.due_date = date.today() + timedelta(days=1)
        elif task.frequency == "weekly":
            task.due_date = date.today() + timedelta(weeks=1)
        task.completed = False