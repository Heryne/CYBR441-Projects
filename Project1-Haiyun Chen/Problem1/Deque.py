from Student import Student

# @Author: Haiyun Chen
# @Date  : 2026/9/13 16:32
# @File  : Deque.py

class Deque:
    """A double-ended queue implemented with a doubly linked list.

    Nodes are Student objects themselves, each Student has prev or next,
    supports push or pop on both ends, search by name, and remove by name.
    """
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

# -------------- helper function --------------
    def isEmpty(self):
        return self._size == 0

    def getSize(self):
        return self._size

    def __len__(self):
        return self._size

    def __str__(self):
        """
        Returns a string showing the deque size and contents front to back.
        """
        names = []
        cur = self._head
        while cur is not None:
            names.append(cur.getName())
            cur = cur.next
        return f"Deque(front -> back):\n{names}"

# -------------- push --------------
    def addFront(self, student:Student):
        """Inserts a student at the front of the deque.

        Args:
            student: the student to insert.
                Its prev or next pointers are rewritten to link it at the head.
        """
        student.prev = None
        student.next = self._head
        if self._head is not None:
            self._head.prev = student
        else:
            self._tail = student
        self._head = student
        self._size += 1

    def addBack(self, student:Student):
        """Inserts a student at the back of the deque.

        Args:
            student: the student to insert.
                Its prev or next pointers are rewritten to link it at the tail.
        """
        student.next = None
        student.prev = self._tail
        if self._tail is not None:
            self._tail.next = student
        else:
            self._head = student
        self._tail = student
        self._size += 1

# -------------- pop --------------
    def removeFront(self):
        """Removes and returns the student at the front.

        Returns:
            the removed Student, or None if the deque is empty.
        """
        if self._head is None:
            return None
        removed = self._head
        self._head = removed.next
        if self._head is not None:
            self._head.prev = None
        else:
            self._tail = None
        removed.prev = removed.next = None
        self._size -= 1
        return removed

    def removeBack(self):
        """Removes and returns the student at the back.

        Returns:
            the removed Student, or None if the deque is empty.
        """
        if self._tail is None:
            return None
        removed = self._tail
        self._tail = removed.prev
        if self._tail is not None:
            self._tail.next = None
        else:
            self._head = None
        removed.prev = removed.next = None
        self._size -= 1
        return removed

# -------------- search --------------
    def search(self, name:str):
        """Checks whether a student with the given name exists.

        Args:
            name: the name to search for.
        Returns:
            True if a matching student is found, False otherwise.
        """
        cur = self._head
        while cur is not None:
            if cur.getName() == name:
                return True
            cur = cur.next
        return False

# -------------- remove --------------
    def remove(self, name:str):
        """Removes the first student whose name matches.
        Walks the deque from front to back and unlinks the first match.

        Args:
            name: the name to search for.
        Returns:
            True if a matching student is found, False otherwise.
        """
        cur = self._head
        while cur is not None:
            if cur.getName() == name:
                if cur.prev is not None:
                    cur.prev.next = cur.next
                else:
                    self._head = cur.next
                if cur.next is not None:
                    cur.next.prev = cur.prev
                else:
                    self._tail = cur.prev
                cur.prev = cur.next = None
                self._size -= 1
                return True
            cur = cur.next
        return False