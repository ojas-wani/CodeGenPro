Python
class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace('-', '').replace(' ', '')
        n = len(number)

        if n <= 4:
            return '-'.join(number)

        formatted = []
        i = 0
        while i < n:
            if i + 2 <= n:
                formatted.append(number[i:i+2])
                i += 2
            else:
                formatted.append(number[i:])
                break

        while len(formatted) < 3:
            i = 0
            j = 1
            while j < n:
                if number[i:j] not in formatted:
                    formatted.insert(0, number[i:j])
                    n -= len(number[i:j])
                    break
                i += 1
                j += 1
                if j >= n:
                    break

        return '-'.join(formatted)