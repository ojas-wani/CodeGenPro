from typing import List

class Solution:
    """
    This class is used to find the number of students who are doing their homework at a given time.
    """
    def __init__(self):
        """
        Constructor
        """
        pass

    def busy_student(self, start_time: List[int], end_time: List[int], query_time: int) -> int:
        """
        This function finds the number of students who are doing their homework at a given time.

        Args:
        start_time (List[int]): A list of integers representing the start time of each student's homework.
        end_time (List[int]): A list of integers representing the end time of each student's homework.
        query_time (int): An integer representing the time for which we need to find the number of students doing their homework.

        Returns:
        int: The number of students who are doing their homework at the query time.
        """
        count = 0
        """
        Initialize a variable to store the count of students doing their homework.
        """
        for i in range(len(start_time)):
            """
            Iterate over the start and end times of each student.
            """
            if start_time[i] <= query_time <= end_time[i]:
                """
                Check if the query time lies within the start and end times of each student. If yes, increment the count.
                """
                count += 1
        return count
        """
        Return the count of students doing their homework at the query time.
        """