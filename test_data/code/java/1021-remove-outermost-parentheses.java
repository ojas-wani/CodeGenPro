class Solution {
    public String removeOuterParentheses(String s) {
        StringBuilder sb = new StringBuilder();
        int open = 0;

        for (char c : s.toCharArray()) {
            if (c == '(') open++;
            if (c == ')') open--;

            if (open > 0) sb.append(c);
        }

        return sb.toString();
    }
}