from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import date

# Create owner
owner = Owner("Fatima")

# Create two pets
dog = Pet("Biscuit", "dog")
cat = Pet("Mochi", "cat")

# Add tasks to Biscuit (out of order on purpose)
dog.add_task(Task("Evening walk", "18:00", 30, "high", "daily", due_date=date.today()))
dog.add_task(Task("Morning walk", "08:00", 30, "high", "daily", due_date=date.today()))
dog.add_task(Task("Feeding", "07:00", 10, "high", "daily", due_date=date.today()))

# Add tasks to Mochi
cat.add_task(Task("Medication", "09:00", 5, "high", "daily", due_date=date.today()))
cat.add_task(Task("Playtime", "15:00", 20, "medium", "daily", due_date=date.today()))

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create scheduler
scheduler = Scheduler(owner)

# Print today's schedule sorted by time
print("=== Today's Schedule ===")
for task in scheduler.sort_by_time():
    status = "✓" if task.completed else "✗"
    print(f"[{status}] {task.time} — {task.description} ({task.duration_minutes} min) [{task.priority}]")

# Print any conflicts
print("\n=== Conflict Check ===")
conflicts = scheduler.detect_conflicts()
if conflicts:
    for warning in conflicts:
        print(f"⚠️  {warning}")
else:
    print("No conflicts found.")