
# @Author: Haiyun Chen
# @Date  : 2026/9/13 16:54
# @File  : BinarySearchTree.py

from Node import Node

class BinarySearchTree:
    """A binary search tree of integer payloads.

    Supports insertion, deletion, search and three depth-first traversals (inorder, preorder, postorder).
    No balancing is done.
    """
    def __init__(self):
        self._root = None
        self._size = 0

    # --------------- helper function ---------------
    def isEmpty(self) -> bool:
        return self._root is None

    def getSize(self) -> int:
        return self._size

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        """Returns a string with the tree size and inorder contents."""
        return f"Binary Search Tree\ninorder = {self.inorder()}"

    # --------------- insertion ---------------
    def insert(self, payload) -> None:
        """Inserts a payload into the tree. Duplicate are ignored.

        Args:
            payload: the integer value to insert.
        """
        if self._root is None:
            self._root = Node(payload)
            self._size += 1
            return
        cur = self._root
        while True:
            if payload < cur.getPayload():
                if cur.hasLeft():
                    cur = cur.getLeft()
                else:
                    cur.setLeft(Node(payload))
                    self._size += 1
                    return
            elif payload > cur.getPayload():
                if cur.hasRight():
                    cur = cur.getRight()
                else:
                    cur.setRight(Node(payload))
                    self._size += 1
                    return
            else:
                return

    # --------------- deletion ---------------
    def delete(self, payload:int) -> bool:
        """Deletes a payload from the tree.

        Handles the three standard BST cases: leaf, one child and two children using inorder successor.

        Args:
            payload: the integer value to delete.
        Returns:
            True if a node was removed, False if the payload was not found.
        """
        cur = self._root
        parent = None
        while cur is not None and cur.getPayload() != payload:
            parent = cur
            if payload < cur.getPayload():
                cur = cur.getLeft()
            else:
                cur = cur.getRight()
        if cur is None:
            return False
        if cur.hasLeft() and cur.hasRight():
            succ_parent = cur
            succ = cur.getRight()
            while succ.hasLeft():
                succ_parent = succ
                succ = succ.getLeft()
            cur.setPayload(succ.getPayload())
            child = succ.getRight()
            if succ_parent.getLeft() is succ:
                succ_parent.setLeft(child)
            else:
                succ_parent.setRight(child)
            self._size -= 1
            return True
        if cur.hasLeft():
            child = cur.getLeft()
        else:
            child = cur.getRight()
        if parent is None:
            self._root = child
        elif parent.getLeft() is cur:
            parent.setLeft(child)
        else:
            parent.setRight(child)
        self._size -= 1
        return True

    # --------------- search ---------------
    def search(self, payload:int) -> bool:
        """Searches for a payload in the tree.

        Args:
            payload: the integer value to look for.
        Returns:
            True if the payload exists, False otherwise.
        """
        cur = self._root
        while cur is not None:
            if payload == cur.getPayload():
                return True
            if payload < cur.getPayload():
                cur = cur.getLeft()
            else:
                cur = cur.getRight()
        return False

    # --------------- traversal ---------------
    def inorder(self) -> list:
        """Returns payloads in ascending order (left, root, right)

        Iterative version using an explicit stack -> temp. No recursion.

        Returns:
            A list of payloads in sorted order.
        """
        result = []
        temp = []
        cur = self._root
        while cur is not None or temp:
            while cur is not None:
                temp.append(cur)
                cur = cur.getLeft()
            cur = temp.pop()
            result.append(cur.getPayload())
            cur = cur.getRight()
        return result

    def preorder(self) -> list:
        """Returns payloads in preorder (root, left, right)

        Iterative version using an explicit stack -> temp. No recursion.

        Returns:
            A list of payloads in preorder.
        """
        result = []
        if self._root is None:
            return result
        temp = [self._root]
        while temp:
            cur = temp.pop()
            result.append(cur.getPayload())
            if cur.hasRight():
                temp.append(cur.getRight())
            if cur.hasLeft():
                temp.append(cur.getLeft())
        return result

    def postorder(self) -> list:
        """Returns payloads in preorder (left, right, root)

        Iterative version using an explicit stack -> temp. No recursion.

        Returns:
            A list of payloads in postorder.
        """
        result = []
        if self._root is None:
            return result
        temp1 = [self._root]
        temp2 = []
        while temp1:
            cur = temp1.pop()
            temp2.append(cur)
            if cur.hasLeft():
                temp1.append(cur.getLeft())
            if cur.hasRight():
                temp1.append(cur.getRight())
        while temp2:
            result.append(temp2.pop().getPayload())
        return result