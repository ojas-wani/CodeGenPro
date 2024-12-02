Python
from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        """
        This function counts the number of items that match the given rule.
        
        Args:
            items (List[List[str]]): A list of lists where each sublist contains the type, color, and name of an item.
            ruleKey (str): The key used to identify the type of rule that should be applied.
            ruleValue (str): The value used to match the specified rule.
        
        Returns:
            int: The number of items that match the given rule.
        """
        count = 0
        key_map = {"type": 0, "color": 1, "name": 2}
        for item in items:
            if item[key_map[ruleKey]] == ruleValue:
                count += 1
        return count

pip install typing