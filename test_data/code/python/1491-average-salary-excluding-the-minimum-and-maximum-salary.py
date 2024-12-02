Python
from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        mini = min(salary)
        maxi = max(salary)
        return sum(salary) - mini - maxi / (len(salary) - 2.0)