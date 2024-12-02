py
class Solution:
    """
    Description: 
    In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, 
    and move any character from words[i] to any position in words[j].

    Return true if you can make every string in words equal using any number of operations, 
    and false otherwise.

    Example 1:
    Input: words = ["abc","aabc","bc"]
    Output: true
    Explanation: Move the first 'a' in words[1] to the front of words[2], 
    to make words[1] = "abc" and words[2] = "abc". 
    All the strings are now equal to "abc", so return true.

    Example 2:
    Input: words = ["ab","a"]
    Output: false
    Explanation: It is impossible to make all the strings equal using the operation.

    Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of lowercase English letters.
    """

from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        """
        This function checks if we can make every string in words equal using any number of operations.
        :param words: A list of strings.
        :return: True if we can make every string equal, False otherwise.
        """
        if not words:
            return True  # An empty list is considered equal

        total_chars = {}
        for word in words:
            for char in word:
                if char not in total_chars:
                    total_chars[char] = 0
                total_chars[char] += 1

        all_chars_equal = all(count % len(words) == 0 for count in total_chars.values())  # Check if all counts are multiples of word count
        all_chars_divisible = all(val // len(words) == total_chars.get(chr(i), 0) for i, val in enumerate(total_chars.values()))  # Check if all counts are equal

        return all_chars_equal and all_chars_divisible