Python
class Solution:
    def generateTheString(self, n: int) -> str:
        res = ''
        for i in range(n):
            if i % 2 == 0:
                res += 'a'
            else:
                res += 'b'
        return res