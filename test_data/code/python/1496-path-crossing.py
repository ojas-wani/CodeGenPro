Python
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = set((0, 0))
        for dir in path:
            if dir == 'N':
                y += 1
            elif dir == 'S':
                y -= 1
            elif dir == 'E':
                x += 1
            elif dir == 'W':
                x -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False