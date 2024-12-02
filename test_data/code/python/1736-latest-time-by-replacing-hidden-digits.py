class Solution:
    def maximumTime(self, time: str) -> str:
        res = list(time)
        for i, c in enumerate(time):
            if c == '?':
                if i == 0:
                    res[i] = '2'
                elif i == 1:
                    res[i] = '3'
                elif i == 3:
                    res[i] = '5' if any(c == '?' for c in res[0:3]) else '9'
                else:
                    res[i] = '0' if any(c == '?' for c in res[0:2]) else '9'
        return ''.join(res)