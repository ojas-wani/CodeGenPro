Python
"""
This problem is to solve the day number of the year given a date in the format of YYYY-MM-DD.
The day number of the year is calculated by converting the date to a datetime object and then getting its timetuple() which returns a time.struct_time object. The tm_yday attribute of this object represents the day of the year (1 <= day_name <= 365).

"""
from datetime import datetime

class Solution:
    """
    This class is used to solve the problem of finding the day number of the year given a date in the format of YYYY-MM-DD.
    """
    def day_of_year(self, date: str) -> int:
        """
        This method is used to find the day number of the year given a date in the format of YYYY-MM-DD.
        
        Args:
        date (str): The date in the format of YYYY-MM-DD.
        
        Returns:
        int: The day number of the year.
        """
        year, month, day = map(int, date.split('-'))
        return datetime(year, month, day).timetuple().tm_yday


# Testing the code with given examples
solution = Solution()
print(solution.day_of_year("2019-01-09"))  # Output: 9
print(solution.day_of_year("2019-02-10"))  # Output: 41