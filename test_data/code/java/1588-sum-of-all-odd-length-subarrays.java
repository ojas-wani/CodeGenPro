class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int n = arr.length;
        int totalSum = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if ((j - i + 1) % 2 != 0) {
                    totalSum += Arrays.stream(arr, i, j + 1).sum();
                }
            }
        }

        return totalSum;
    }
}