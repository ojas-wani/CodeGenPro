class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        res = set()
        cur_num = ''
        for char in word:
            if char.isdigit():
                cur_num += char
            else:
                if cur_num:
                    cur_num = cur_num.lstrip('0')
                    if cur_num:
                        res.add(cur_num)
                    cur_num = ''
        if cur_num:
            cur_num = cur_num.lstrip('0')
            if cur_num:
                res.add(cur_num)
        return len(res)