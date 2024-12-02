Python
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_map = {}
        for num in arr1:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        sorted_output = []
        for num in arr2:
            if num in count_map:
                sorted_output.extend([num] * count_map[num])
                del count_map[num]
        
        for num in sorted(count_map.keys()):
            sorted_output.extend([num] * count_map[num])
        
        return sorted_output