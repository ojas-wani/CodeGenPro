Python
import heapq
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldier_count = [(row.count(1), i) for i, row in enumerate(mat)]
        heapq.heapify(soldier_count)
        weakest_rows = []
        while soldier_count and k > 0:
            k -= 1
            weakest_rows.append(heapq.heappop(soldier_count)[1])
        return weakest_rows