from Student import Student
from Deque import Deque

# @Author: Haiyun Chen
# @Date  : 2026/9/19 22:11
# @File  : driver.py

def main():
    dq = Deque()

    # -------------- push --------------
    print("\n-------------- push --------------")
    dq.addBack(Student("imStudent1", 19, 3.0))
    dq.addBack(Student("imStudent2", 20, 3.2))
    dq.addFront(Student("imStudent3", 20, 3.4))
    dq.addFront(Student("imStudent4", 21, 3.6))
    print(dq)

    # -------------- search --------------
    print("\n-------------- search --------------")
    print(f"Search [Student 1]: {dq.search('imStudent1')}")
    print(f"Search [Student who]: {dq.search('Studentwho')}")

    # -------------- remove --------------
    print("\n-------------- remove --------------")
    print(f"Remove [Student 1]: {dq.remove('imStudent1')}")
    print(f"Remove [Student 1]: {dq.remove('imStudent1')}")
    print(f"Remove [Student 3]: {dq.remove('imStudent3')}")
    print(f"Remove [Student 3]: {dq.remove('imStudent3')}")
    print(dq)

    # -------------- pop --------------
    print("\n-------------- pop --------------")
    print(f"Remove Front: {dq.removeFront()}")
    print(f"Remove Back: {dq.removeBack()}")
    print(f"\nAfter:\n{dq}")

    # -------------- empty --------------
    print("\n-------------- empty --------------")
    print(f"Is the queue empty: {dq.isEmpty()}")
    print(f"Size: {dq.getSize()}")


if __name__ == '__main__':
    main()