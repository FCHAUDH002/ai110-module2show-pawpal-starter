from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import date, timedelta

def test_task_completion():
    """Test that mark_complete() changes the task's status."""
    task = Task("Morning walk", "08:00", 30, "high", "daily")
    task.mark_complete()
    assert task.completed == False  # resets for recurring tasks

def test_task_addition():
    """Test that adding a task to a pet increases its task count."""
    pet = Pet("Biscuit", "dog")
    task = Task("Feeding", "07:00", 10, "high", "daily")
    pet.add_task(task)
    assert len(pet.get_tasks()) == 1

def test_sort_by_time():
    """Test that tasks are returned in chronological order."""
    owner = Owner("Fatima")
    dog = Pet("Biscuit", "dog")
    dog.add_task(Task("Evening walk", "18:00", 30, "high", "daily"))
    dog.add_task(Task("Morning walk", "08:00", 30, "high", "daily"))
    dog.add_task(Task("Feeding", "07:00", 10, "high", "daily"))
    owner.add_pet(dog)
    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()
    times = [t.time for t in sorted_tasks]
    assert times == ["07:00", "08:00", "18:00"]

def test_recurrence_logic():
    """Test that marking a daily task complete sets due date to tomorrow."""
    task = Task("Feeding", "07:00", 10, "high", "daily", due_date=date.today())
    task.mark_complete()
    assert task.due_date == date.today() + timedelta(days=1)

def test_conflict_detection():
    """Test that scheduler flags two tasks at the same time."""
    owner = Owner("Fatima")
    dog = Pet("Biscuit", "dog")
    cat = Pet("Mochi", "cat")
    dog.add_task(Task("Morning walk", "08:00", 30, "high", "daily"))
    cat.add_task(Task("Medication", "08:00", 5, "high", "daily"))
    owner.add_pet(dog)
    owner.add_pet(cat)
    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) > 0