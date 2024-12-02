class Solution {
    public int countLargestGroup(int n) {
        int[] count = new int[37];
        int max = 0;
        for (int i = 1; i <= n; i++) {
            int sum = 0;
            for (char c : Integer.toString(i).toCharArray()) {
                sum += c - '0';
            }
            count[sum]++;
            max = Math.max(max, count[sum]);
        }
        return Arrays.stream(count).filter(x -> x == max).count();
    }
}