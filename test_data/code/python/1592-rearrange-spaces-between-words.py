Python
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        num_of_words = len(words)
        total_spaces = text.count(' ')
        
        if num_of_words == 1:
            extra_spaces = total_spaces
            space_between_words = 0
        else:
            extra_spaces = total_spaces - (num_of_words - 1)
            space_between_words = total_spaces // (num_of_words - 1)
        
        result = ' '.join(words)
        if extra_spaces > 0:
            result += ' ' * extra_spaces
        
        return result