# File name should be in snake_case and has a docstring

"""
Module: Defanging an IP Address
Description: This module is designed to defang a given IPv4 address.
"""

class Solution:
    """
    Class Definition: Defanging an IP Address
    Attributes: None
    Methods: defang_ip_addr
    """

    """
    Method: defang_ip_addr
    Description: This method defangs a given IPv4 address by replacing every period with '[.]'.
    Parameters: address (str) - A valid IPv4 address
    Returns: str - A defanged IPv4 address
    """
    def defang_ip_addr(self, address: str) -> str:
        # Replace every period in the address with '[.]'
        defanged_address = address.replace('.', '[.]')
        return defanged_address

# Example usage
solution = Solution()
print(solution.defang_ip_addr("1.1.1.1"))  # Output: "1[.]1[.]1[.]1"
print(solution.defang_ip_addr("255.100.50.0"))  # Output: "255[.]100[.]50[.]0"