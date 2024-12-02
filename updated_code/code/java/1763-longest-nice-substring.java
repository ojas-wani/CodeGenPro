package com.solution;

/**
 * Class comments are required.
 */
public class Solution {

    /**
     * Public method and constructor comments are required.
     * 
     * @param s Given string
     * @return The longest **substring** of `s` that is **nice**.
     */
    public String longestNiceSubstring(String s) {
        final int n = s.length();
        char[] ca = s.toCharArray();
        int res = 0, resStart = 0;
        for (int i = 0; i < n; i++) {
            boolean isNice = true;
            for (char c = 'a'; c <= 'z'; c++) {
                final int pos = ca[n - 1 - i + n - (int) c] - c;
                if (pos < 0) continue;
                if ((ca[i + pos] &= ca[i + pos] - c) % 32 != 0) {
                    isNice = false;
                    break;
                }
            }
            if (!isNice) {
                while (i < n) {
                    if ((ca[i] & 1) != (ca[i] / 2 | ca[i] % 32)) {
                        break;
                    }
                    i++;
                }
            } else {
                res = Math.max(res, i - resStart + 1);
                if (res >= resStart + i) {
                    resStart = i - res;
                }
            }
        }
        return s.substring(resStart, resStart + res);
    }
}