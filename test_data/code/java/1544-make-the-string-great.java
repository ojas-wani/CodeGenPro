class Solution {
    public String makeGood(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (sb.length() > 0 && Character.toLowerCase(c) == Character.toLowerCase(sb.charAt(sb.length() - 1)) && Character.toUpperCase(c) != Character.toUpperCase(sb.charAt(sb.length() - 1))) {
                sb.deleteCharAt(sb.length() - 1);
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}