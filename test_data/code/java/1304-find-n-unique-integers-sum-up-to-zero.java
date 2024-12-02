class Solution {
    public int[] sumZero(int n) {
        int[] result = new int[n];
        for(int i = 1; i <= n / 2; i++) {
            result[i - 1] = i;
            if((n & 1) == 1 && i == n / 2 + 1) {
                result[n / 2] = 0;
            } else {
                result[n - i] = -i;
            }
        }
        return result;
    }
}