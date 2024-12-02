Python
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed_list = []
        for i in range(0, len(nums), 2):
            freq = nums[i]  # frequency
            val = nums[i+1]  # value
            decompressed_list.extend([val]*freq)  # add the sublist to the decompressed list
        return decompressed_list