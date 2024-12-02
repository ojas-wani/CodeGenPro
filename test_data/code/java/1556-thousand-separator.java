class Solution {
    public String thousandSeparator(int n) {
        if (n < 1000) {
            return String.valueOf(n);
        }
        String str = String.valueOf(n);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            sb.append(str.charAt(i));
            if ((i + 1) % 3 == 0 && i != str.length() - 1) {
                sb.append('.');
            }
        }
        return sb.toString();
    }
}