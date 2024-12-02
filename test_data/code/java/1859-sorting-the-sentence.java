class Solution {
    public String sortSentence(String s) {
        String[] words = s.split(" ");
        StringBuilder sb = new StringBuilder();
        Arrays.sort(words, (a, b) -> Integer.parseInt(a.substring(a.length() - 1)) - Integer.parseInt(b.substring(b.length() - 1)));
        for (String word : words) {
            sb.append(word.substring(0, word.length() - 1)).append(" ");
        }
        return sb.toString().trim();
    }
}