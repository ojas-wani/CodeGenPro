class Solution {
    public String restoreString(String s, int[] indices) {
        char[] ca = s.toCharArray();
        for(int i = 0; i < s.length(); i++) {
            ca[indices[i]] = s.charAt(i);
        }
        return new String(ca);
    }
}