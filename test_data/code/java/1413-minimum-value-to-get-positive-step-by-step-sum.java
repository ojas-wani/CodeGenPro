class Solution {
    public int minStartValue(int[] nums) {
        int sum = 0;
        int minStartValue = 0;

        for (int num : nums) {
            sum += num;
            minStartValue = Math.max(minStartValue, 1 - sum);
        }

        return Math.max(minStartValue, 1);
    }
}