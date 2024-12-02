"""
A class to solve issues based on description and reports.
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the `day`, `month` and
`year` respectively.

Return the answer as one of the following values `{"Sunday", "Monday",
"Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}`.
"""

from datetime import datetime

class Solution:
    """
    A class to solve the given date to its corresponding day of the week.
    """

    """
    A function to convert the given date to its corresponding day of the week.
    
    Parameters: 
    day (int): The day of the month.
    month (int): The month of the year.
    year (int): The year.

    Returns: 
    str: The corresponding day of the week for the given date.
    """

    def day_of_the_week(self, day: int, month: int, year: int) -> str:
        date = datetime(year, month, day)
        return date.strftime("%A")


# Example usage
solution = Solution()
print(solution.day_of_the_week(31, 8, 2019))  # Output: "Saturday"
print(solution.day_of_the_week(18, 7, 1999))  # Output: "Sunday"
print(solution.day_of_the_week(15, 8, 1993))  # Output: "Sunday"