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
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

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
