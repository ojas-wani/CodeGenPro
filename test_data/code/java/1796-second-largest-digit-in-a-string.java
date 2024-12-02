class Solution {
    public int secondHighest(String s) {
        Set<Integer> set = new HashSet<>();
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                set.add(Integer.parseInt(String.valueOf(c)));
            }
        }
        if (set.size() < 2) {
            return -1;
        }
        int secondHighest = -1;
        for (int num : set) {
            if (num > secondHighest && num != Collections.max(set)) {
                secondHighest = num;
            }
        }
        return secondHighest;
    }
}