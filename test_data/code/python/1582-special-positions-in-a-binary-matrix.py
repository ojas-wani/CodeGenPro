class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        for i in range(m):
            yes = []
            for j in range(n):
                if mat[i][j] == 1:
                    yes.append([i, j])
                    for k in range(m):
                        if k != i and mat[k][j] == 1:
                            break
                    for k in range(n):
                        if k != j and mat[i][k] == 1:
                            break
                    break
            for item in yes:
                res += 1
        return res