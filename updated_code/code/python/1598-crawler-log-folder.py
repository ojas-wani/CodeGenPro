from typing import List

class Solution:
    """
    This class provides a solution to the LeetCode problem 1598: Crawler Log Folder.

    It uses a stack to keep track of the folder path and calculates the minimum number of operations needed to go back to the main folder.

    :param logs: A list of strings representing the log operations performed by the user.
    :return: The minimum number of operations needed to go back to the main folder.
    """
    def min_operations(self, logs: List[str]) -> int:
        """
        This method calculates the minimum number of operations needed to go back to the main folder.

        :param logs: A list of strings representing the log operations performed by the user.
        :return: The minimum number of operations needed to go back to the main folder.
        """
        stack = []
        res = 0
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log != "./":
                stack.append(log[1:])
        return res + len(stack)