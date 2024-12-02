class Solution {
    public int numPrimeArrangements(int n) {
        int MOD = 1000000007;
        int count = 0;
        boolean[] isPrime = new boolean[n + 1];
        for (int i = 2; i <= n; i++) {
            isPrime[i] = true;
        }
        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) {
                count++;
            }
        }
        long res = 1;
        for (int i = 1; i <= Math.min(count, n - count); i++) {
            res = res * i % MOD;
        }
        for (int i = 1; i <= Math.abs(count - n); i++) {
            res = res * i % MOD;
        }
        return (int) res;
    }
}