Python
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        coordinates = [(i, j) for i in range(rows) for j in range(cols)]
        distances = [(abs(i - rCenter) + abs(j - cCenter), [i, j]) for i, j in coordinates]
        distances.sort()
        return [cell for _, cell in distances]