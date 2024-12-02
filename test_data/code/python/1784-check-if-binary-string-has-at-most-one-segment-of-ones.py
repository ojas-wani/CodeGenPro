class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count = 0
        for c in s:
            if c == '1':
                count += 1
                if count > 1:
                    return False
        return True