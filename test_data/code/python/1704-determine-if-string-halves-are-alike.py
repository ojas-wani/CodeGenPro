class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        
        half = len(s) // 2
        
        a = set(s[:half]).intersection(vowels)
        b = set(s[half:]).intersection(vowels)
        
        return len(a) == len(b)