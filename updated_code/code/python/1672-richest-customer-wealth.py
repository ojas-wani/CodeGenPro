from typing import List

class Solution:
    """
    This class defines a method maximumWealth to find the wealth of the richest customer.
    
    Attributes:
    None

    Methods:
    maximumWealth(accounts) -> int: Returns the maximum wealth of the customers.
    """

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        This method finds the maximum wealth of the customers.
        
        Args:
        accounts (List[List[int]]): A 2D list where each inner list represents the amount of money a customer has in each bank.
        
        Returns:
        int: The maximum wealth of the customers.
        """
        max_wealth = 0  # Initialize the maximum wealth to 0
        for customer in accounts:
            wealth = sum(customer)  # Calculate the wealth of each customer
            max_wealth = max(max_wealth, wealth)  # Update the maximum wealth if the current customer's wealth is greater
        return max_wealth  # Return the maximum wealth