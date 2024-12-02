class Solution {
    public int maxRepeating(String sequence, String word) {
        int max = 0;
        for (int i = 0; i <= sequence.length() - word.length(); i++) {
            String temp = sequence.substring(i, i + word.length());
            if (temp.equals(word)) {
                int k = 1;
                int j = i + word.length();
                while (j < sequence.length() && sequence.substring(j - word.length(), j).equals(word)) {
                    j += word.length();
                    k++;
                }
                max = Math.max(max, k);
            }
        }
        return max;
    }
}