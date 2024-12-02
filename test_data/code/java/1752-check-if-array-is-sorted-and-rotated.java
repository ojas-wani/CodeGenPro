class Solution {
    public boolean check(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                if (i == 0 || nums[i] < nums[i - 1]) return false;
                return true;
            }
        }
        return nums[0] <= nums[n - 1];
    }
}