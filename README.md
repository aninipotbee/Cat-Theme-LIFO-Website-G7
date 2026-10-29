
# Meowspace: Website Remix + LIFO Stack Challenge

**Course:** Data Structures and Algorithms  
**Section:** CS2C  
**Group:** 7

## Team Members

- Jenica Vallente
- Kent Ezra Sungahid
- Psalm Esther Nissi Waslo
- Daisy Jane Manabat
- Anilynn Pangca

## 1. Project Overview

Meowspace is a cat-themed website featuring a workspace and a Recovery Tray for removed items. The backend uses a **Last-In, First-Out (LIFO) stack**, meaning the most recently removed item is restored first.

For example, if items are removed in the order **A → B → C**, they must be restored in the order **C → B → A**.

## 2. Project Features

- Cat-themed website redesign.
- Recovery Tray for removed items.
- LIFO stack implementation using Python.
- Stack operations: `push()`, `pop()`, `peek()`, `is_empty()`, `size()`, and `to_list()`.
- Stack representation designed to support database persistence.
- Testing and evidence of the restoration sequence.

## 3. Project Structure

The following is a suggested structure. Update it to match the actual repository.

```text
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
```

## 4. Requirements

- Python
- Dependencies listed in `requirements.txt`
- Database configuration, if required

## 5. Installation and Running

1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Create and activate a virtual environment if needed.
4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Initialize the database if required by the project.
6. Start the application using its actual entry point. For example, if `run.py` is the entry point:

   ```bash
   python run.py
   ```

7. Open the local website address displayed by the application, if applicable.

**Note:** Verify these instructions against the actual repository before submitting.

## 6. Backend Implementation

**File:** `backend/stack.py`

The `Stack` class stores removed item IDs in a Python list. The end of the list represents the top of the stack, allowing items to be added and removed efficiently.

### Stack Operations

| Method | Description | Time Complexity |
|---|---|---|
| `push(item)` | Adds an item to the top of the stack. | O(1) amortized |
| `pop()` | Removes and returns the top item. | O(1) |
| `peek()` | Returns the top item without removing it. | O(1) |
| `is_empty()` | Checks whether the stack is empty. | O(1) |
| `size()` | Returns the number of items. | O(1) |
| `to_list()` | Returns a copy of the stack from bottom to top. | O(n) |

### How LIFO Works

LIFO stands for **Last In, First Out**. The last item added to the stack is the first item removed.

Example:

```python
from backend.stack import Stack

recovery = Stack()

recovery.push("A")
recovery.push("B")
recovery.push("C")

print(recovery.peek())       # C
print(recovery.pop())        # C
print(recovery.pop())        # B
print(recovery.pop())        # A
print(recovery.is_empty())   # True
```

The stack initially contains:

```python
["A", "B", "C"]
```

- **A** is the oldest item at the bottom.
- **B** is in the middle.
- **C** is the newest item at the top.

Therefore, `pop()` returns C first, followed by B and A.

### Representation and Persistence

The `to_list()` method returns a new list in **bottom-to-top order**, matching the database contract for saving stack data in SQLite.

For example:

```python
["A", "B", "C"]
```

When saving and loading the stack, this order must be preserved to maintain the correct restoration sequence.

Because `to_list()` returns a copy, modifying the returned list does not directly change the internal stack.

When `pop()` or `peek()` is called on an empty stack, the implementation raises an `IndexError` with the message:

`The recovery tray is empty.`

The alias `HistoryBuffer = Stack` allows the same implementation to be imported using either name.

## 7. Recovery Sequence

The main requirement is to demonstrate the correct restoration order.

1. Remove item A.
2. Remove item B.
3. Remove item C.
4. Restore the removed items.

**Expected result: C → B → A**

This behavior must be demonstrated through the actual website and not only through a code example.

## 8. Testing

| Test | Action | Expected Result |
|---|---|---|
| Push | Push A, B, and C. | Stack order is A, B, C from bottom to top. |
| Pop | Pop three times. | Returns C, then B, then A. |
| Peek | Peek when C is on top. | Returns C without removing it. |
| Empty check | Check an empty stack. | Returns `True`. |
| Size | Push three items and pop one. | Size changes from 3 to 2. |
| Empty pop | Pop from an empty stack. | Raises `IndexError`. |
| Empty peek | Peek at an empty stack. | Raises `IndexError`. |
| Copy check | Modify the list returned by `to_list()`. | Internal stack remains unchanged. |
| Website restoration | Remove A, B, and C. | Restores C, B, and A. |
| Persistence | Refresh or restart the application. | Saved order is preserved, if persistence is implemented. |

## 9. Evidence and Documentation

- Before-and-after screenshots of the website redesign.
- Screenshot or recording showing the A → B → C removal and C → B → A restoration sequence.
- Evidence of persistence after refreshing or restarting the application.
- Final test results.

## 10. Team Contributions

| Role | Assigned Member |
|---|---|
| Team Lead & Integration | Jenica Vallente |
| Backend / Stack Developer | Anilynn Pangca |
| Frontend / UI Developer | Kent Sungahid |
| Data & Feature Developer | Psalm Esther Nissi Waslo |
| QA & Documentation Lead | Daisy Mantalaba |


## 11. References and Attribution

- **Original starter project:** [(https://github.com/franku69/Website-Stack-Data-Structure)]
