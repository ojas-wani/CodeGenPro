from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        cnt = Counter(s)
        res = []
        while cnt:
            # sort small characters
            temp = sorted([c for c in cnt if cnt[c] > 0])
            while temp and cnt[temp[0]] > 0:
                cnt[temp[0]] -= 1
                res.append(temp.pop(0))
            
            # sort large characters
            temp = sorted([c for c in cnt if cnt[c] > 0], reverse=True)
            while temp and cnt[temp[0]] > 0:
                cnt[temp[0]] -= 1
                res.append(temp.pop(0))

        return ''.join(res)