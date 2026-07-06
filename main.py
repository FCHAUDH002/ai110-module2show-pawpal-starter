from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import date

# Create owner
owner = Owner("Fatima")

# Create two pets
dog = Pet("Biscuit", "dog")
cat = Pet("Mochi", "cat")

# Add tasks OUT OF ORDER on purpose to test sorting
dog.add_task(Task("Evening walk", "18:00", 30, "high", "daily", due_date=date.today()))
dog.add_task(Task("Morning walk", "08:00", 30, "high", "daily", due_date=date.today()))
dog.add_task(Task("Feeding", "07:00", 10, "high", "daily", due_date=date.today()))

# Add a conflicting task to test conflict detection
cat.add_task(Task("Medication", "08:00", 5, "high", "daily", due_date=date.today()))
cat.add_task(Task("Playtime", "15:00", 20, "medium", "daily", due_date=date.today()))

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create scheduler
scheduler = Scheduler(owner)

# Test sorting
print("=== Today's Schedule (Sorted by Time) ===")
for task in scheduler.sort_by_time():
    status = "✓" if task.completed else "✗"
    print(f"[{status}] {task.time} — {task.description} ({task.duration_minutes} min) [{task.priority}]")

# Test filtering by pet name
print("\n=== Biscuit's Tasks Only ===")
for task in scheduler.filter_tasks(pet_name="Biscuit"):
    print(f"  {task.time} — {task.description}")

# Test filtering by completion status
print("\n=== Incomplete Tasks Only ===")
for task in scheduler.filter_tasks(status=False):
    print(f"  {task.time} — {task.description}")

# Test conflict detection
print("\n=== Conflict Check ===")
conflicts = scheduler.detect_conflicts()
if conflicts:
    for warning in conflicts:
        print(f"⚠️  {warning}")
else:
    print("No conflicts found.")

# Test recurring task logic
print("\n=== Recurring Task Test ===")
feeding = dog.get_tasks()[2]  # Feeding task
print(f"Before: {feeding.description} — completed: {feeding.completed}, due: {feeding.due_date}")
feeding.mark_complete()
print(f"After: {feeding.description} — completed: {feeding.completed}, due: {feeding.due_date}")