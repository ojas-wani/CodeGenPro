from typing import List

class Solution:
    """
    This class defines a method to calculate the average salary of employees
    excluding the minimum and maximum salary.
    """

    """
    This method takes a list of unique salaries as input and returns the
    average salary excluding the minimum and maximum salary.
    """

    def average(self, salary: List[int]) -> float:
        """
        Returns the average salary of employees excluding the minimum and
        maximum salary.

        Args:
        salary (List[int]): A list of unique salaries.

        Returns:
        float: The average salary excluding the minimum and maximum salary.
        """
        mini = min(salary)
        maxi = max(salary)
        return sum(i for i in salary if i != mini and i != maxi) / (len(salary) - 2.0)