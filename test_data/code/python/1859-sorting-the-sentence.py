class Solution:
    def sortSentence(self, s: str) -> str:
        words = ["" for _ in range(9)]
        temp = [i for i in s.split(' ')]
        for word in temp:
            for char in word:
                if char.isdigit():
                    index = int(char)
                    words[index - 1] = (words[index - 1] + word.replace(str(index), '') + ' ')
                    break
        # Remove trailing space, join and return
        return ' '.join(map(lambda x: x.strip(), words)).strip()