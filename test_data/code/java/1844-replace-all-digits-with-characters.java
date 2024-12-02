class Solution {
    public String replaceDigits(String s) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c;
            if (i % 2 == 1) {
                c = (char) ((s.charAt(i - 1) - 'a' + (s.charAt(i) - '0')) % 26 + 'a');
            } else {
                c = s.charAt(i);
            }
            result.append(c);
        }
        return result.toString();
    }
}