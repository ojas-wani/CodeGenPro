import java.util.HashMap;

public class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> cnt = new HashMap<>();
        for (int n : nums) {
            cnt.put(n, cnt.getOrDefault(n, 0) + 1);
        }
        for (int n : nums) {
            if (cnt.get(n) > nums.length / 2) {
                return n;
            }
        }
        return -1;
    }
}