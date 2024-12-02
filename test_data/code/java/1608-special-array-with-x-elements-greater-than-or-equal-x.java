class Solution {
    public int specialArray(int[] nums) {
        Arrays.sort(nums);
        
        for (int i = 0; i <= nums.length; i++) {
            if (i == nums.length - nums.length % 2) {
                if (i == nums.length || nums[i - 1] < i) {
                    return i;
                } else {
                    break;
                }
            }
        }
        
        return -1;
    }
}