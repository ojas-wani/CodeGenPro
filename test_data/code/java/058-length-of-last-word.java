class Solution {
    public int lengthOfLastWord(String s) {
        String[] words = s.trim().split("\\s+"); // remove leading and trailing spaces and split by one or more spaces
        return words[words.length - 1].length(); // return the length of the last word
    }
}