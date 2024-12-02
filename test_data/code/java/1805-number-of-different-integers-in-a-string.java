class Solution {
    public int numDifferentIntegers(String word) {
        String[] nums = word.split("[a-z]+");
        Set<String> set = new HashSet<>();
        for (String num : nums) {
            num = num.trim();
            if (!num.isEmpty()) {
                set.add(trimLeadingZeros(num));
            }
        }
        return set.size();
    }

    private String trimLeadingZeros(String num) {
        while (!num.isEmpty() && num.charAt(0) == '0') {
            num = num.substring(1);
        }
        return num;
    }
}