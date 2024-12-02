class Solution:
    def reformat(self, s: str) -> str:
        char_count = [0, 0]
        for char in s:
            if char.isdigit():
                char_count[0] += 1
            else:
                char_count[1] += 1
        if abs(char_count[0] - char_count[1]) > 1:
            return ""
        result = []
        if char_count[0] > char_count[1]:
            prev = 'd'
        else:
            prev = 'l'
        for char in s:
            if char_count[0] > char_count[1]:
                if char.isdigit():
                    result.append(char)
                    char_count[0] -= 1
            else:
                if char.isalpha():
                    result.append(char)
                    char_count[1] -= 1
            if prev == 'd' and char.isdigit():
                prev = 'l'
            elif prev == 'l' and char.isalpha():
                prev = 'd'
        return ''.join(result)