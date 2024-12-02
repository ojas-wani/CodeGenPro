class Solution {
    public String reformatNumber(String number) {
        number = number.replaceAll("[^0-9]", "");
        StringBuilder sb = new StringBuilder();
        int n = number.length();
        for (int i = 0; i < n; i += 2) {
            if (i + 2 <= n) {
                sb.append(number.substring(i, i + 2));
            } else {
                sb.append(number.substring(i));
            }
            if (i + 2 < n) {
                sb.append("-");
            }
        }
        return sb.toString();
    }
}