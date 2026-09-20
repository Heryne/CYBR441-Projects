
# @Author: Haiyun Chen
# @Date  : 2026/9/13 15:47
# @File  : Student.py

###
# AI CODE
# Agent name: DeepSeek
# Model: DeepSeek V4.1 Flash
# Use: The following code was written by me, but I put my work into the model to improve and perfect code blocks, and added appropriate helper functions.
###

class Student:
    """Represents a student record that also acts as a doubly linked list node.

    Stores name, age, and gpa, with validation on each filed. Also holds prev and next pointers.
    This Student class can be linked into a Deque directly without a separate Node class.
    """
    MIN_AGE = 0
    MAX_AGE = 150
    MIN_GPA = 0.0
    MAX_GPA = 4.0

    def __init__(self, name:str="None", age:int=0, gpa:float=0.0):
        self.setName(name)
        self.setAge(age)
        self.setGPA(gpa)
        self.prev = None
        self.next = None

    # ---------------- accessor / getters ----------------
    def getName(self) -> str:
        return self._name

    def getAge(self) -> int:
        return self._age

    def getGPA(self) -> float:
        return self._gpa

    # ---------------- mutator / setters ----------------
    def setName(self, name:str) -> None:
        """
        Args:
            name: a non-empty string, leading and trailing whitespace, is stripped before storing.
        Raises:
            ValueError: if name is not a string or is empty/whitespace only.

        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        self._name = name.strip()

    def setAge(self, age:int) -> None:
        """

        Args:
            age: an int between Student.MIN_AGE and Student.MAX_AGE
        Raises:
            TypeError: if age is not an int or is bool.
            ValueError: if age is outside [MIN_AGE, MAX_AGE].

        """
        if not isinstance(age, int) or isinstance(age, bool):
            raise TypeError("age must be an int")
        if not self.MIN_AGE <= age <= self.MAX_AGE:
            raise ValueError(f"age must be between {self.MIN_AGE} and {self.MAX_AGE}")
        self._age = age

    def setGPA(self, gpa:float) -> None:
        """

        Args:
            gpa: a number between Student.MIN_GPA and Student.MAX_GPA
                Stored as a float.
        Raises:
            TypeError: if gpa is not a number or is a bool.
            ValueError: if gpa is outside [MIN_GPA, MAX_GPA]

        """
        if not isinstance(gpa, (int, float)) or isinstance(gpa, bool):
            raise TypeError("gpa must be a number")
        if not self.MIN_GPA <= gpa <= self.MAX_GPA:
            raise ValueError(f"gpa must be between {self.MIN_GPA} and {self.MAX_GPA}")
        self._gpa = float(gpa)

    # ---------------- helper function ----------------
    def __str__(self) -> str:
        return f"Student(name={self._name!r}, age={self._age}, gpa={self._gpa})"

    def __repr__(self) -> str:
        return self.__str__()

    # compare if two students are equal
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return (
                self._name == other._name
                and self._age == other._age
                and self._gpa == other._gpa
        )

###
# End AI CODE Block
###