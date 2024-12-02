Python
from collections import Counter

class Solution:
    def sort_string(self):
        """
        Reorder the string using the following algorithm:

        1. Pick the **smallest** character from `s` and **append** it to the result.
        2. Pick the **smallest** character from `s` which is greater than the last appended character to the result and **append** it.
        3. Repeat step 2 until you cannot pick more characters.
        4. Pick the **largest** character from `s` and **append** it to the result.
        5. Pick the **largest** character from `s` which is smaller than the last appended character to the result and **append** it.
        6. Repeat step 5 until you cannot pick more characters.
        7. Repeat the steps from 1 to 6 until you pick all characters from `s`.

        Args:
        s (str): Input string.

        Returns:
        str: The result string after sorting `s` with this algorithm.
        """
        cnt = Counter(self.s)
        res = []
        while cnt:
            # sort small characters
            small_chars = sorted([c for c in cnt if cnt[c] > 0])
            while small_chars and cnt[small_chars[0]] > 0:
                cnt[small_chars[0]] -= 1
                res.append(small_chars.pop(0))

            # sort large characters
            large_chars = sorted([c for c in cnt if cnt[c] > 0], reverse=True)
            while large_chars and cnt[large_chars[0]] > 0:
                cnt[large_chars[0]] -= 1
                res.append(large_chars.pop(0))

        return ''.join(res)

    def __init__(self, s: str):
        self.s = s

    def sort_string(self) -> str:
        return self.sort_string()