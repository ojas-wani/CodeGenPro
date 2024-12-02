package com.leetcode;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int numPrimeArrangements(int n) {
        long MOD = 1_000_000_007;
        int primeCount = 0;
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
                primeCount++;
            }
        }

        long res = 1;
        for (int i = 1; i <= Math.min(primeCount, n - primeCount); i++) {
            res = res * i % MOD;
        }
        for (int i = 1; i <= Math.abs(primeCount - n); i++) {
            res = res * i % MOD;
        }
        return (int) res;
    }
}