from typing import List

class Solution:
    """
    Solve the slowest key problem where the key of the keypress that had the longest duration is desired.

    Parameters:
    releaseTimes (List[int]): A sorted list of release times.
    keysPressed (str): A string representing the keys pressed in the desired order.

    Returns:
    str: The key of the keypress that had the longest duration.
    If there are multiple such keypresses, return the lexicographically largest key of the keypresses.
    """

    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        """
        Find the key of the keypress that had the longest duration.

        Args:
        releaseTimes (List[int]): A sorted list of release times.
        keysPressed (str): A string representing the keys pressed in the desired order.

        Returns:
        str: The key of the keypress that had the longest duration.
        If there are multiple such keypresses, return the lexicographically largest key of the keypresses.
        """
        
        max_duration = releaseTimes[0]
        result = keysPressed[0]
        
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration > max_duration:
                max_duration = duration
                result = keysPressed[i]
            elif duration == max_duration:
                result = max(result, keysPressed[i])
        
        return result