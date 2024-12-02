class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        if (s1.length() != s2.length()) return false;
        int diff1 = -1, diff2 = -1;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                if (diff1 != -1) return false;
                diff1 = i;
            }
        }
        if (diff1 == -1) return true;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) == s2.charAt(diff1)) {
                if (diff2 != -1) return false;
                diff2 = i;
            }
        }
        return diff2 != -1 && s1.charAt(diff1) == s2.charAt(diff2);
    }
}