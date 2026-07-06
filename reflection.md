# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.

For my initial design, I identified three core actions a user should be able to perform. First, a user should be able to add a pet by entering its name and species. Second, a  user should be able to schedule a care task like a walk or feeding for a specific pet at a specific time. Third, a user should be able to generate and view a daily schedule of all their pet's tasks.

- What classes did you include, and what responsibilities did you assign to each?

For my class design, I chose four classes of task, pet, owner, and scheduler. The Task class represents a single care activity and holds information like the description, time, duration, priority, frequency, and whether it has been completed. The Pet class represents one animal and holds its name, species, and a list of tasks. The Owner class represents the person using the app and manages a list of pets. The Scheduler class is the brain of the system and is responsible for sorting tasks by time, filtering tasks, detecting conflicts, and handling recurring tasks.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

My design did not change significantly after AI review. The main feedback was that the Scheduler should retrieve all tasks through the Owner's get_all_tasks() method rather than accessing each pet's tasks directly.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?

My scheduler considers time as the main constraint, sorting all tasks chronologically so the owner can follow a clear daily plan. It also considers completion status and pet name as filters so the owner can focus on what still needs to be done.

- How did you decide which constraints mattered most?

I decided these constraints mattered most because a pet owner primarily needs to know what to do and when to do it. Time and completion status are the most practical pieces of information for planning a daily routine.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.

One tradeoff my scheduler makes is that it only checks for exact start times when detecting conflicts. For example, if a task starts at 08:00 and lasts 60 minutes, and another task starts at 08:30, the scheduler would not flag that as a conflict.

- Why is that tradeoff reasonable for this scenario?

This is reasonable because the app is meant to be simple, and the owner can decide for themselves whether two overlapping tasks are actually a problem and take action accordingly. Implementing duration-based overlap detection would require converting time strings to datetime objects and comparing ranges, which adds complexity. 


---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?

I used AI tools throughout this project for design brainstorming, code generation, and debugging. In the design phase, I asked the AI to help me identify the four main classes and their responsibilities. During implementation, I used it to generate the class skeletons and fill in the logic for sorting, filtering, and conflict detection.

- What kinds of prompts or questions were most helpful?

The most helpful prompts were specific ones, like asking how to sort tasks by time in HH:MM format using a lambda function, and asking the AI to explain why a test was failing and whether the bug was in my test or my logic.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.

One moment where I did not accept the AI suggestion as-is was when the mark_complete() method was generated outside of the Task class instead of inside it.

- How did you evaluate or verify what the AI suggested?

The code looked correct at first glance but was not indented properly, which caused an AttributeError when I tried to call it. I caught this by running the code and reading the error message, then went back and fixed the indentation manually.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?

I tested task completion, task addition, sorting correctness, recurrence logic, and conflict detection. 

- Why were these tests important?

Task completion and task addition were important to test because they are the most fundamental operations in the system. Sorting correctness was important because the whole schedule depends on tasks being 
in the right order. Recurrence logic and conflict detection were important because they are the more complex algorithms and most likely to have bugs.

**b. Confidence**

- How confident are you that your scheduler works correctly?

I am very confident that my scheduler works correctly for the core behaviors since all 5 tests pass.

- What edge cases would you test next if you had more time?

If I had more time, I would test edge cases like a pet with no tasks, a task with an invalid time format, and two tasks that overlap in duration but not in start time.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied with how the scheduling algorithms turned out. Sorting, filtering, and conflict detection all work correctly and are backed by passing tests. Building and testing the backend logic in the terminal first before touching the UI made everything a lot easier to debug.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If I had another iteration, I would improve the conflict detection to check for duration overlaps instead of just exact start time matches. I would also connect the UI more fully to the backend so that pets and tasks added in the browser are actually stored in the Owner and Pet classes instead of just a session state list.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

The most important thing I learned is that AI is a useful tool for generating code quickly, but you still need to understand what the code is doing in order to catch mistakes. The AI generated the mark_complete() method outside of the class and it looked fine at first, but running the code and reading the error message is what actually caught the bug.