from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        result = []
        
        for i in range(m):
            min_val = min(matrix[i])
            min_idx = matrix[i].index(min_val)
            
            for j in range(n):
                if matrix[i][j] == min_val and max(column(j, matrix)) == min_val:
                    result.append(min_val)
                    break
                    
        return result

def column(j, matrix):
    return [row[j] for row in matrix]