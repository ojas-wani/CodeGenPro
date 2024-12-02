from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        res = 0
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log != "./":
                stack.append(log[1:])
            else:
                continue
        return res + len(stack)