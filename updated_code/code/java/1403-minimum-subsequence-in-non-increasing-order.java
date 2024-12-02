//Package declaration
package test;

import java.util.*;

class Solution {
    //Class comment
    public List<Integer> minSubsequence(int[] nums) {
        //Method comment
        Arrays.sort(nums);
        int sum = 0, left = 0;
        for (int right = nums.length - 1; left < right; ) {
            sum += nums[right--];
            left++;
            while (left < nums.length && sum >= nums[left]) {
                left++;
            }
        }
        List<Integer> res = new ArrayList<>();
        int j = nums.length - 1;
        for (int i = nums.length - 1; i >= left; i--) {
            if (nums[i] > nums[j]) {
                res.add(nums[i]);
                j--;
            }
        }
        return res;
    }
}