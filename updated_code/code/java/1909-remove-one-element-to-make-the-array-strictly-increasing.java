// No changes needed except adding package declaration
package codereview;

import java.util.Arrays;

class Solution {
    public boolean canBeIncreasing(int[] nums) {
        int count = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] <= nums[i - 1]) {
                count++;
                if (Arrays.copyOfRange(nums, 0, i).length > 2 && Arrays.copyOfRange(nums, 0, i - 1).length > 2) {
                    if (nums[i - 1] > nums[i - 2]) {
                        return true;
                    }
                }
            }
        }
        return count <= 1;
    }
}