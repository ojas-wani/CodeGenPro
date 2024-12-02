class Solution {
    public String largestOddNumber(String num) {
        for (int i = num.length() - 1; i >= 0; i--) {
            if ((num.charAt(i) - '0') % 2 != 0) {
                for (int j = i; j >= 0; j--) {
                    if (isOddInteger(num.substring(j, i + 1))) {
                        return num.substring(j, i + 1);
                    }
                }
            }
        }
        return "";
    }

    private boolean isOddInteger(String s) {
        int val = Integer.parseInt(s);
        return val % 2 != 0;
    }
}