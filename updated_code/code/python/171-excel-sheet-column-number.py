class Solution:
    """
    The class Solution contains the method titleToNumber to convert column title to number.
    
    The method titleToNumber takes a string columnTitle as input and returns the corresponding column number.
    
    It does this by initializing a variable result to 0 and then iterating over the characters in the columnTitle. 
    For each character, it multiplies the result by 26 (the number of uppercase English letters) and adds the position of the character (A=1, B=2, ..., Z=26) in the range of values.
    
    Finally, it returns the result as the column number.
    """
    def titleToNumber(self, column_title: str) -> int:
        """
        Convert the column title to number in an Excel sheet.
        
        This method takes a string column title as input, converts it to a number 
        and returns the number.
        
        Parameters:
        column_title (str): A string representing the column title in an Excel sheet.
        
        Returns:
        int: The corresponding column number in the Excel sheet.
        """
        result = 0
        for char in column_title:
            result = result * 26 + ord(char) - ord('A') + 1
        return result