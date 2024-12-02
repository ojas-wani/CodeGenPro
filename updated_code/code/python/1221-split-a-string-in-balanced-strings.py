Python
class balanced_string_splitter:
    """
    This class is used to solve the problem of splitting a balanced string into the maximum number of balanced strings.
    """
    
    def __init__(self):
        """
        This function initializes a balanced string splitter.
        """
        
        pass
    
    def balanced_string_split(self, s: str) -> int:
        """
        This function takes a balanced string as input and returns the maximum number of balanced strings that can be obtained by splitting the string.
        
        Parameters:
        s (str): The balanced string to be split.
        
        Returns:
        int: The maximum number of balanced strings that can be obtained by splitting the string.
        """
        
        res = 0
        count = 0
        for c in s:
            if c == 'L':
                count += 1
            else:
                count -= 1
            if count == 0:
                res += 1
        return res
Python
import unittest
from balanced_string_splitter import balanced_string_split

class TestBalancedStringSplitter(unittest.TestCase):

    def test_balanced_string_split(self):
        self.assertEqual(balanced_string_split("RLRRLLRLRL"), 4)
        self.assertEqual(balanced_string_split("RLRRRLLRLL"), 2)
        self.assertEqual(balanced_string_split("LLLLRRRR"), 1)
        self.assertEqual(balanced_string_split("LLLLRR"), 1)
        self.assertEqual(balanced_string_split("RR"), 1)

if __name__ == '__main__':
    unittest.main()