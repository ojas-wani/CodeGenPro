class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        diff_count = 0
        diffs = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_count += 1
                diffs.append(i)
                if diff_count > 2:
                    return False

        return diff_count == 2