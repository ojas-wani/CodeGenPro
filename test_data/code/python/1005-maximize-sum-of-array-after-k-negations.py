class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort() # Sort the array in ascending order
        count = 0 # Count of negative numbers
        for num in nums:
            if num < 0: # If number is negative
                count += 1 # Increment the count
                num = -num # Flip the number
            if count >= k: # If count of negative numbers is more than or equal to k
                break # Stop the loop
            nums[nums.index(num)] = num # Update the array with the flipped number
        nums.sort(reverse=True) # Sort the array in descending order
        return sum(nums) # Calculate and return the sum