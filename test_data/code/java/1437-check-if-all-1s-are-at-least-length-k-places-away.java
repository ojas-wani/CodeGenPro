class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == 1 && i + 1 < k) {
                return false;
            }
            if (nums[i] == 1 && i + 1 >= k) {
                i += k - 1;
            }
        }
        return true;
    }
}