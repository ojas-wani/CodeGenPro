class Solution {
    public String reformat(String s) {
        int letterCount = 0;
        int digitCount = 0;
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                letterCount++;
            } else {
                digitCount++;
            }
        }
        if (Math.abs(letterCount - digitCount) > 1) {
            return "";
        }
        StringBuilder result = new StringBuilder();
        int letterPtr = 0;
        int digitPtr = 0;
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                if (digitPtr < digitCount) {
                    result.append(c);
                    digitPtr++;
                } else {
                    result.append(c);
                    letterPtr++;
                }
            } else {
                if (letterPtr < letterCount) {
                    result.append(c);
                    letterPtr++;
                } else {
                    result.append(c);
                    digitPtr++;
                }
            }
        }
        return result.toString();
    }
}