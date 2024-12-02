"""
Module to calculate the number of days between two dates.

This module provides a solution to calculate the number of days between two dates.
The dates are given as strings in the format 'YYYY-MM-DD'.

Example:
    Input: date1 = "2019-06-29", date2 = "2019-06-30"
    Output: 1

    Input: date1 = "2020-01-15", date2 = "2019-12-31"
    Output: 15

Constraints:
    * The given dates are valid dates between the years 1971 and 2100.
"""

import datetime

class DateCalculator:
    """
    Class to calculate the number of days between two dates.
    """

    def __init__(self):
        pass

    def days_between_dates(self, date1: str, date2: str) -> int:
        """
        Calculate the number of days between two dates.

        Args:
            date1 (str): The first date in the format 'YYYY-MM-DD'.
            date2 (str): The second date in the format 'YYYY-MM-DD'.

        Returns:
            int: The number of days between the two dates.
        """
        dt1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
        dt2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
        return abs((dt2 - dt1).days)

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.days_between_dates("2019-06-29", "2019-06-30"))  # Output: 1
    print(calculator.days_between_dates("2020-01-15", "2019-12-31"))  # Output: 15