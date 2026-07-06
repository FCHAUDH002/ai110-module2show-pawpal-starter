# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

=== Today's Schedule ===
[✗] 07:00 — Feeding (10 min) [high]
[✗] 08:00 — Morning walk (30 min) [high]
[✗] 09:00 — Medication (5 min) [high]
[✗] 15:00 — Playtime (20 min) [medium]
[✗] 18:00 — Evening walk (30 min) [high]

=== Conflict Check ===
No conflicts found.

## 🧪 Testing PawPal+

My tests cover task completion, task addition, sorting correctness, recurrence logic, and conflict detection.

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
================================================================================================ test session starts ================================================================================================
platform darwin -- Python 3.13.13, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/fatimachaudhry/Downloads/Codepath/ai110-module2show-pawpal-starter
plugins: anyio-4.13.0
collected 5 items                                                                                                                                                                                                   

tests/test_pawpal.py .....                                                                                                                                                                                    [100%]

================================================================================================= 5 passed in 0.03s =================================================================================================
```

Confidence Level: 5/5 stars. All 5 tests pass and cover the core scheduling behaviors.

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts all tasks by time in HH:MM format |
| Filtering | `Scheduler.filter_tasks()` | Filters by pet name or completion status |
| Conflict handling | `Scheduler.detect_conflicts()` | Flags tasks scheduled at the exact same time |
| Recurring tasks | `Task.mark_complete()` | Automatically updates due date for daily and weekly tasks |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. Open the app by running `streamlit run app.py` in the terminal.
2. Enter an owner name and pet name in the Quick Demo Inputs section.
3. Select the species from the dropdown menu.
4. Add a few tasks by entering a task title, duration, and priority then clicking "Add task".
5. Click "Generate schedule" to see all tasks sorted by time in a table.
6. If two tasks are scheduled at the same time, a conflict warning will appear.
7. If no conflicts are found, a success message will appear.

Key Scheduler behaviors:
- Tasks are always displayed in chronological order using `Scheduler.sort_by_time()`
- Conflicts are detected when two tasks share the same start time using `Scheduler.detect_conflicts()`
- Daily and weekly tasks automatically update their due date when marked complete

Sample CLI output from running `main.py`:

=== Today's Schedule (Sorted by Time) ===
[✗] 07:00 — Feeding (10 min) [high]
[✗] 08:00 — Morning walk (30 min) [high]
[✗] 08:00 — Medication (5 min) [high]
[✗] 15:00 — Playtime (20 min) [medium]
[✗] 18:00 — Evening walk (30 min) [high]

=== Biscuit's Tasks Only ===
  18:00 — Evening walk
  08:00 — Morning walk
  07:00 — Feeding

=== Incomplete Tasks Only ===
  18:00 — Evening walk
  08:00 — Morning walk
  07:00 — Feeding
  08:00 — Medication
  15:00 — Playtime

=== Conflict Check ===
⚠️  Conflict at 08:00: 'Morning walk' and 'Medication'

=== Recurring Task Test ===
Before: Feeding — completed: False, due: 2026-07-05
After: Feeding — completed: False, due: 2026-07-06

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
