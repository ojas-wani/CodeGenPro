from math import inf
from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        x, i = 1, 0
        while candies > 0:
            if candies >= x:
                res[i] += x
                candies -= x
                x += 1
            else:
                res[i] += candies
                candies = 0
            if i == num_people - 1:
                i = 0
            else:
                i += 1
        return res