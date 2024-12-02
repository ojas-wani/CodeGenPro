from collections import deque
from typing import List

class Solution:
    """
    This is the solution class for the problem.
    It defines a method countStudents that counts the number of students unable to eat lunch.
    """
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        This method counts the number of students unable to eat lunch.
        Args:
        students (List[int]): A list of integers representing the preferences of students.
        sandwiches (List[int]): A list of integers representing the types of sandwiches.

        Returns:
        int: The number of students unable to eat lunch.
        """
        student_queue = deque(students)
        eaten_students = 0

        while student_queue and student_queue[0] != sandwiches[0]:
            student_queue.append(student_queue.popleft())

        eaten_students = len(students) - len(student_queue)

        return eaten_students