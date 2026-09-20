
# @Author: Haiyun Chen
# @Date  : 2026/9/13 16:54
# @File  : Node.py

###
# AI CODE
# Agent name: DeepSeek
# Model: DeepSeek V4.1 Flash
# Use: The following code was written by me, but I put my work into the model to improve and perfect code blocks, and added appropriate helper functions.
###

class Node:
    """Represents a single node in a binary search tree.

    Each node stores an integer payload and optional left/right children.
    """
    def __init__(self, payload:int):
        self._payload = payload
        self._left = None
        self._right = None

    def getPayload(self) -> int:
        return self._payload

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def setPayload(self, payload:int) -> None:
        """Sets the node's payload after validating it.

        Args:
            payload: an integer value
        Raises:
            TypeError: if payload is not an int or is a bool.

        """
        if not isinstance(payload, int) or isinstance(payload, bool):
            raise TypeError("payload must be an int")
        self._payload = payload

    def setLeft(self, node) -> None:
        self._left = node

    def setRight(self, node) -> None:
        self._right = node

    def isLeaf(self) -> bool:
        """Returns True if this node has no children."""
        return self._left is None and self._right is None

    def hasLeft(self) -> bool:
        """Returns True if this node has a left child."""
        return self._left is not None

    def hasRight(self) -> bool:
        """Returns True if this node has a right child."""
        return self._right is not None

    def __str__(self) -> str:
        return f"Node(payload={self._payload})"

    def __repr__(self) -> str:
        return self.__str__()


###
# End AI CODE Block
###