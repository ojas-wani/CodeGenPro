class Solution {
    public boolean makeEqual(String[] words) {
        int[] charCount = new int[26];
        int totalChars = 0;

        // Count the total number of characters and count the occurrences of each character
        for (String word : words) {
            int[] wordCount = new int[26];
            for (char c : word.toCharArray()) {
                wordCount[c - 'a']++;
            }
            for (int i = 0; i < 26; i++) {
                charCount[i] += wordCount[i];
            }
            totalChars += word.length();
        }

        // Check if all strings can be made equal
        for (int count : charCount) {
            if (count % (totalChars / words.length) != 0) {
                return false;
            }
        }
        return true;
    }
}