class Solution:
    def modifyString(self, s: str) -> str:
        result = list(s)
        for i in range(len(result)):
            if result[i] == '?':
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if (i > 0 and result[i-1] == c) or (i < len(result) - 1 and result[i+1] == c):
                        continue
                    result[i] = c
                    break
        return ''.join(result)