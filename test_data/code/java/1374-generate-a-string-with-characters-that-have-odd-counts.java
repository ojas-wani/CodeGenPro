class Solution {
    public String generateTheString(int n) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append('p');
        }
        if (n > 1) {
            sb.append('a');
        }
        return sb.toString().substring(0, n);
    }
}