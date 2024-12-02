class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        max_alt = 0
        for i in range(len(gain)):
            altitude += gain[i]
            max_alt = max(max_alt, altitude)
        return max_alt