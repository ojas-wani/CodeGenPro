class Solution {
    public List<Boolean> prefixesDivBy5(int[] nums) {
        List<Boolean> answer = new ArrayList<>();
        int sum = 0;
        for (int num : nums) {
            sum = (sum * 2 + num) % 5;
            answer.add(sum == 0);
        }
        return answer;
    }
}