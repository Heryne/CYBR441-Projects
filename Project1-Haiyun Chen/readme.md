# Project-1
Course: CYBR 441

Instructor: Nathan Roth

Author: Haiyun Chen:
`chanh@lopers.unk.edu`

***
## Project Purpose
This project is designed to finish the problems from requirements, and enhance understanding of nodes, deque, binary search tree and traversal.

## AI Usage(If Permitted)
Model: DeepSeek V4.1 Flash

Summary: AI was used only in `Problem1/Student.py` and `Problem2/Node.py` to review and improve the existing code blocks and to suggest appropriate helper functions. All other files were written entirely by me, including `Problem1/Deque.py`, `Problem2/BinarySearchTree.py` and all `driver.py`. 

AI-generated code is located in
- `Problem1/Student.py` lines 13-103
- `Problem2/Node.py` lines 13-67

***
## Problem 1 - Student Class and Deque
### Files
| File         | Description                                                                               |
|--------------|-------------------------------------------------------------------------------------------|
| `Student.py` | stores name, age, gpa with validation, holds prev and next pointers as a linked-list node |
| `Deque.py`   | a doubly linked list based deque.                                                         |
| `driver.py`  | tests the deque operations.                                                               |

### Notes
- no separate `Node.py`, `Student.py` instead, stores `prev` and `next`
- `Deque.py`: `_head`, `_tail`, and `_size`

### Functions
- `__init__`
- `accessors`
- `mutators`
- `isEmpty`
- `getSize`
- `__len__`
- `__str__`
- push front: `addFront(student)`
- push back: `addBack(student)`
- pop front: `removeFront()`
- pop back: `removeBack()`
- search by name: `search(name) -> bool`
- remove by name: `remove(name) -> bool`

### Sample
```output

-------------- push --------------
Deque(front -> back):
['imStudent4', 'imStudent3', 'imStudent1', 'imStudent2']

-------------- search --------------
Search [Student 1]: True
Search [Student who]: False

-------------- remove --------------
Remove [Student 1]: True
Remove [Student 1]: False
Remove [Student 3]: True
Remove [Student 3]: False
Deque(front -> back):
['imStudent4', 'imStudent2']

-------------- pop --------------
Remove Front: Student(name='imStudent4', age=21, gpa=3.6)
Remove Back: Student(name='imStudent2', age=20, gpa=3.2)

After:
Deque(front -> back):
[]

-------------- empty --------------
Is the queue empty: True
Size: 0
```

***
## Problem 2 - Binary Search Tree
### Files
| File                  | Description                                        |
|-----------------------|----------------------------------------------------|
| `Node.py`             | stores an integer payload and left/right children. |
| `BinarySearchTree.py` | class with insert, delete, search, and traversals. |
| `driver.py`           | tests the BST operations.                          |

### Notes
- a separate `Node.py`: `_payload`, `_left`, `_right`
- `BinarySearchTree.py`: `_root`, `_size`

### Functions
- `__init__`
- `isEmpty`
- `getSize`
- `__len__`
- `__str__`
- `insertion`
- `deletion`
- `search`
- Traversals: `inorder`, `preorder`, `postorder`

### Sample
```output

--------------- insertion ---------------
Binary Search Tree
inorder = [20, 30, 40, 50, 60, 70, 80]

--------------- search ---------------
Search -> 40: True
Search -> 99: False

--------------- traversal ---------------
inorder -> [20, 30, 40, 50, 60, 70, 80]
preorder -> [50, 30, 20, 40, 70, 60, 80]
postorder -> [20, 40, 30, 60, 80, 70, 50]

--------------- deletion ---------------
Delete -> 20: True
Delete -> 50: True
After: inorder -> [30, 40, 60, 70, 80]
```

***
## Problem 3
### a. How much time did you spend on these two problems?
Since I created these files, I spent a few days to finish these problems.
Most time, I have to figure out deque's prev and next pointers, correctly in head, tail, and algorithms. 

### b. How would you rate the difficulty of these two problems?
Difficult: 8/10 in total

I rated it 8/10 because they were a large project to finish, and a large amount of text that requires standardization needs to pay attention to many things, such as whether the function naming in my class is standardized and meets the project's standard requirements.

For documentation in Style Guide, I haven't written it before, so I need to learn how to complete these requirements.

I simply learned some basic concepts and usage from previous classes but some expressions are very unfamiliar. Such as docstring, argument or return types and f-string.
Thus, I find some notes from CSDN.net to help me to understanding how deque, BST, and traversals work.

## Overall Structure
```
├── README.md
├── Problem1/
│ ├── Student.py
│ ├── Deque.py
│ └── driver.py
├── Problem2/
│ ├── Node.py
│ ├── BinarySearchTree.py
│ └── driver.py
└── Problem3/
  └── Reflection.py
```