package problems;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    /**
     * Returns the sum of all XOR totals for every subset of the given array.
     *
     * @param nums the input array
     * @return the sum of all XOR totals for every subset
     */
    public int subsetXORSum(int[] nums) {
        int res = 0;
        for (int mask = 0; mask < (1 << nums.length); mask++) {
            int xor = 0;
            List<Integer> subset = new ArrayList<>();
            for (int i = 0; i < nums.length; i++) {
                if (((mask >> i) & 1) == 1) {
                    xor ^= nums[i];
                    subset.add(nums[i]);
                }
            }
            res += xor;
        }
        return res;
    }
}