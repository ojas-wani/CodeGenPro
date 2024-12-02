Python
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        max_len = 0
        res = ""
        
        for i in range(len(s)):
            tmp_set = set()
            for j in range(i, len(s)):
                c = s[j]
                if c in tmp_set:
                    break
                if c.lower() in tmp_set:
                    break
                if c.isupper():
                    tmp_set.add(c.lower())
                else:
                    tmp_set.add(c)
                if len(tmp_set) == 26:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        res = s[i:j+1]
        return res