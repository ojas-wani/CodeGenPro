class Solution:
    def count_good_substrings(self, s: str) -> int:
        """
        This method counts the number of substrings of size three having distinct characters.

        Parameters:
        s (str): The input string.

        Returns:
        int: The number of substrings of size three with distinct characters.
        """
        count = 0
        for i in range(len(s) - 2):
            # Extract the substring of size 3
            substring = s[i:i+3]
            # Check if the substring has distinct characters
            if len(set(substring)) == 3:
                # If distinct, increment the count
                count += 1
        return count