class Solution {
    public int sumBase(int n, int k) {
        int sum = 0;
        while (n > 0) {
            n = n % k;
            sum = sum + n;
            n = n / k;
        }
        return sum;
    }
}