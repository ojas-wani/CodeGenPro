Python
class Solution:
    """
    This class contains the solution for the problem mentioned.
    """
    
    def totalMoney(self, n: int) -> int:
        """
        This function calculates the total amount of money that can be collected in the LeetCode bank.
        
        Parameters:
        n (int): The number of days.
        
        Returns:
        int: The total amount of money.
        """
        n -= 1     # subtract 1 because Monday is 0
        week = n // 7
        remainder = n % 7
        return week * 28 + sum(range(1, 8)) + sum(range(1, remainder + 1))