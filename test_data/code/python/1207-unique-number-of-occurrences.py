Python
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict = Counter(arr)
        return len(set(count_dict.values())) == len(count_dict)