Python
from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)        
        sorted_nums = sorted(count.items(), key=lambda x: (-x[1], -x[0]))
        result = []
        for num, freq in sorted_nums:
            result.extend([num] * freq)
        return result