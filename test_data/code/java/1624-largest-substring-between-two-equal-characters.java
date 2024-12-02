class Solution {
    public int maxLengthBetweenEqualCharacters(String s) {
        int maxLen = -1;
        Map<Character, Integer> map = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (map.containsKey(c)) {
                maxLen = Math.max(maxLen, i - map.get(c) - 1);
            } else {
                map.put(c, i);
            }
        }
        
        return maxLen;
    }
}