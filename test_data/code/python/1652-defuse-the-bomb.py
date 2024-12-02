class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        return [sum((code[(i+k)%n] if k > 0 else code[(i-k)%n]) for i in range(n))]