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
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
