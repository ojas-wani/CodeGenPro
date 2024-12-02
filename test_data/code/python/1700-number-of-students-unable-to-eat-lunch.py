from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_queue = deque(students)
        eaten_students = 0

        while student_queue and student_queue[0] != sandwiches[0]:
            student_queue.append(student_queue.popleft())

        eaten_students = len(students) - len(student_queue)

        return eaten_students