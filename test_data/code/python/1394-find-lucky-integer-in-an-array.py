Python
from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        frequency = Counter(arr)
        lucky_numbers = [num for num, freq in frequency.items() if freq == num]
        return max(lucky_numbers) if lucky_numbers else -1