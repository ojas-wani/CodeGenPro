class Solution {
    public int subsetXORSum(int[] nums) {
        int res = 0;
        for (int mask = 0; mask < (1 << nums.length); mask++) {
            int xor = 0;
            for (int i = 0; i < nums.length; i++) {
                if (((mask >> i) & 1) == 1) {
                    xor ^= nums[i];
                }
            }
            res += xor;
        }
        return res;
    }
}