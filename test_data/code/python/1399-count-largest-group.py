class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Initialize an empty hashmap to store the frequency of each group
        freq = {}
        
        # Initialize the maximum group size and the count of largest groups
        max_size = 0
        max_count = 0
        
        # Iterate over the numbers from 1 to n
        for i in range(1, n + 1):
            # Calculate the sum of the digits of the current number
            dig_sum = sum(int(digit) for digit in str(i))
            
            # Update the frequency of the group
            if dig_sum not in freq:
                freq[dig_sum] = 1
            else:
                freq[dig_sum] += 1
            
            # Update the maximum group size and the count of largest groups
            if freq[dig_sum] > max_count or (freq[dig_sum] == max_count and dig_sum > max_size):
                max_size = dig_sum
                max_count = freq[dig_sum]
        
        # Return the count of largest groups
        return max_count