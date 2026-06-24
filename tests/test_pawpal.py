from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import date

def test_task_completion():
    """Test that mark_complete() changes the task's status to True."""
    task = Task("Morning walk", "08:00", 30, "high", "daily")
    task.mark_complete()
    assert task.completed == True

def test_task_addition():
    """Test that adding a task to a pet increases its task count."""
    pet = Pet("Biscuit", "dog")
    task = Task("Feeding", "07:00", 10, "high", "daily")
    pet.add_task(task)
    assert len(pet.get_tasks()) == 1