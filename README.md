Meowspace: Website Remix + LIFO Stack Challenge
Backend Implementation
Course: Data Structures and Algorithms
Section: CS2C
Group: 7
Team Members
- Jenica Vallente
- Kent Ezra Sungahid
- Psalm Esther Nissi Waslo
- Daisy Jane Manabat
- Anilynn Pangca
1. Project Overview
Meowspace is a cat-themed website concept that includes a workspace and a Recovery Tray for items that have been removed. The backend demonstrates a Last-In, First-Out (LIFO) stack: the most recently removed item is the first one restored.

For example, if items are removed in the order A → B → C, the recovery order is C → B → A. This behavior is the main data-structures requirement of the project.
2. Main Features
The project is designed to demonstrate:
- A redesigned website interface for the Meowspace concept.
- A Recovery Tray that records removed item IDs.
- LIFO restoration, where the newest removed item is restored first.
- Stack operations such as push, pop, and peek.
- A stack representation that can be saved in bottom-to-top order for database persistence.
- Evidence of restoration behavior, persistence, and test results.
The exact interface features and startup steps depend on the files included in the submitted repository. Follow the commands and configuration used by the project.

3. Repository Structure
The submitted repository should include the project source and supporting evidence. A suggested structure is:
repository/
├── frontend/
├── backend/
│   └── stack.py
├── database/
├── tests/
├── challenge/
├── run.py
├── requirements.txt
├── README.md
└── docs/
    ├── STACK_EXPLANATION.md
    ├── TEST_LOG.md
    ├── CONTRIBUTIONS.md
    └── evidence/
        ├── before-home.png
        ├── after-home.png
        ├── recovery-lifo.png
        └── final-test-results.png
Some folders or filenames may differ in the actual repository. Keep this section consistent with the final submitted files.
4. Requirements
- Python installed on the computer.
- The packages listed in requirements.txt.
- The project database and configuration, if required by the implementation.
5. Setup and Run Instructions
1. Clone or download the repository.
2. Open a terminal in the repository's root folder.
3. Create and activate a virtual environment if your project uses one.
4. Install the dependencies:
   pip install -r requirements.txt
5. Follow the project's database initialization instructions, if applicable.
6. Start the application using the actual entry-point command configured in the repository. For example, if run.py is the entry point:
   python run.py
7. Open the local address shown by the application, if it starts a web server.
Before submitting: verify every command above against the repository and test the instructions from a fresh clone or download. Do not commit virtual environments, secret keys, local database files, or other machine-specific generated files.
6. Backend Stack Implementation
File: backend/stack.py

The Stack class stores the IDs of removed items in a Python list. The end of the list represents the top of the stack. This makes adding and removing the top item efficient.
Stack operations
Method	Purpose	Expected time
push(item)	Adds an item ID to the top of the stack.	O(1) amortized
pop()	Removes and returns the newest item ID. Raises IndexError if empty.	O(1)
peek()	Returns the newest item ID without removing it. Raises IndexError if empty.	O(1)
is_empty()	Returns True when the stack has no items.	O(1)
size()	Returns the number of stored item IDs.	O(1)
to_list()	Returns a new list in bottom-to-top order.	O(n)


The constructor accepts an optional iterable of existing items and copies it into the stack's internal list. The alias HistoryBuffer = Stack lets other code use the same implementation under the name HistoryBuffer.
Why is this a LIFO stack?
A stack follows Last In, First Out. The most recently pushed item is at the end of the list, so pop() removes that item first.

Example:
from backend.stack import Stack

recovery = Stack()

recovery.push("A")
recovery.push("B")
recovery.push("C")

print(recovery.peek())    # C
print(recovery.pop())     # C
print(recovery.pop())     # B
print(recovery.pop())     # A
print(recovery.is_empty())  # True
Representation and persistence order
Internally, the stack is stored from bottom to top. For example:
["A", "B", "C"]
Here, A is the oldest item and C is the newest item at the top.

to_list() returns a new list in that same bottom-to-top order. This is useful when saving the stack to SQLite according to the database contract. Because it returns a copy, changing the returned list does not directly change the stack's internal list.

When restoring saved stack data, preserve the same order. Reversing the list during loading or saving can cause the recovery order to become incorrect.
7. Expected Recovery Behavior
The core acceptance check is to remove three items in this order:
1. Remove A.
2. Remove B.
3. Remove C.
4. Restore an item.
The first restored item must be C, followed by B, then A. Confirm this behavior through the actual website and the backend, not just by displaying a hard-coded example.

Also check that:
- peek() shows the newest item without removing it.
- An empty stack reports is_empty() as True.
- Calling pop() or peek() on an empty stack raises IndexError with the message The recovery tray is empty.
- Saved stack data retains the correct order after a refresh or restart, if persistence is implemented.
8. Testing Checklist
Record the actual result of each test in docs/TEST_LOG.md.
Test	Action	Expected result
Stack push	Push A, then B, then C.	Stack order is A, B, C from bottom to top.
LIFO pop	Pop three times.	Returns C, then B, then A.
Peek	Peek when C is on top.	Returns C without changing the stack.
Empty check	Check a new or emptied stack.	is_empty() returns True.
Size	Push three items, then pop one.	Size changes from 3 to 2.
Empty pop	Pop from an empty stack.	Raises the expected IndexError.
Empty peek	Peek at an empty stack.	Raises the expected IndexError.
List copy	Modify the list returned by to_list().	The internal stack remains unchanged.
Website restoration	Remove A → B → C, then restore.	C → B → A is restored.
Persistence	Save, refresh or restart, and inspect the tray.	Saved order is preserved, if implemented.


Include screenshots or a short recording showing the original and redesigned website, the actual A → B → C removal and C → B → A restoration sequence, persistence after refresh or restart, and final test results.
9. Known Limitations
Document limitations observed in the actual project here. Possible areas to check include:
- Whether recovery records persist after restarting the application.
- Whether the database and stack remain synchronized after an item is restored.
- How the interface handles missing or invalid item IDs.
- Whether errors are displayed clearly to users.
Do not list a limitation as resolved unless it has been tested.
10. Team Contributions
Each member should document their own work in docs/CONTRIBUTIONS.md. Include:
- Member name.
- Tasks completed.
- Files created or changed.
- Relevant commits or other evidence.
- A short explanation of the contribution.
The names in the Team Members section identify the group only; they do not imply a specific task assignment.
11. References and Attribution
Credit the original starter project and any external code, assets, or references used. Follow the attribution requirements provided with the assignment. Add the actual source links here:
- Original starter project: [Add source link]
- External assets or references: [Add sources, if applicable]
12. Final Submission Checklist
- [ ] The repository contains the complete source code, not only screenshots or a ZIP file.
- [ ] README.md matches the actual repository structure and startup process.
- [ ] backend/stack.py and the LIFO behavior are explained.
- [ ] docs/STACK_EXPLANATION.md describes representation, operations, persistence order, complexity, and one bug fixed.
- [ ] docs/TEST_LOG.md contains actual test results.
- [ ] docs/CONTRIBUTIONS.md records each member's work and evidence.
- [ ] Screenshots or a recording show the redesign, restoration order, and persistence test.
- [ ] The project has been cloned or downloaded into a fresh folder and tested by following this README.
- [ ] No secrets, virtual environments, or unintended local database files are committed.
- [ ] The final tested version is pushed to the team's GitHub repository.
