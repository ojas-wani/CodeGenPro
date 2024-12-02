import math

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(1, len(points)):
            dx = abs(points[i][0] - points[i-1][0])
            dy = abs(points[i][1] - points[i-1][1])
            dist = math.sqrt(dx**2 + dy**2)
            time += int(math.ceil(dist))
        return time