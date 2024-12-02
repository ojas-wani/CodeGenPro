class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int n = nums.length;
        int[] count = new int[n];
        Arrays.sort(nums);
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            if (!map.containsKey(nums[i])) {
                map.put(nums[i], i);
            }
        }
        
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = map.getOrDefault(nums[i] - 1, -1);
        }
        
        return result;
    }
}