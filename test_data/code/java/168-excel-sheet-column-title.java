class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder result = new StringBuilder();
        while (columnNumber > 0) {
            columnNumber--;
            result.insert(0, (char)('A' + columnNumber % 26));
            columnNumber /= 26;
        }
        return result.toString();
    }
}

System.out.println(new Solution().convertToTitle(1)); // outputs "A"
System.out.println(new Solution().convertToTitle(28)); // outputs "AB"
System.out.println(new Solution().convertToTitle(701)); // outputs "ZY"