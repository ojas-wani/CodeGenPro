py
import string

# Solution class with a method makeGood
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

# Utility class with a method remove_adjacent_duplicates
class Helper:
    def remove_adjacent_duplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

# Remove adjacent duplicate characters from a string
def remove_adjacent_duplicates(s):
    stack = []
    for char in s:
        if stack and abs(ord(stack[-1]) - ord(char)) == 32:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

# Print the output
s = "leEeetcode"
output = remove_adjacent_duplicates(s)
print(output)