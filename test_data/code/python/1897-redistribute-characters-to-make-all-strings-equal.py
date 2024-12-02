Python
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if not words:
            return True

        total_chars = {}
        for word in words:
            for char in word:
                if char not in total_chars:
                    total_chars[char] = 0
                total_chars[char] += 1

        freq = []
        for count in total_chars.values():
            if count % len(words) > 0:
                return False
            freq.append(count // len(words))

        return all(count % len(words) == 0 for count in total_chars.values())