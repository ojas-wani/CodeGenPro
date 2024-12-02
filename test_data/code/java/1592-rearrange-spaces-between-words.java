class Solution {
    public String reorderSpaces(String text) {
        String[] words = text.trim().split("\\s+");
        int totalSpaces = text.length() - text.trim().length();
        int wordsCount = words.length;
        
        if (wordsCount == 1) {
            return words[0] + String.format("%" + totalSpaces + "s", " ").replace(" ", "");
        }
        
        int spacesBetweenWords = totalSpaces / (wordsCount - 1);
        int leftOverSpaces = totalSpaces % (wordsCount - 1);
        
        StringBuilder result = new StringBuilder();
        for (String word : words) {
            result.append(word);
            if (result.length() < text.length()) {
                for (int i = 0; i < spacesBetweenWords; i++)
                    result.append(' ');
                if (leftOverSpaces > 0) {
                    result.append(' ');
                    leftOverSpaces--;
                }
            }
        }
        return result.toString();
    }
}