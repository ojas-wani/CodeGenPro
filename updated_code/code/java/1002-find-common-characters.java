import java.util.*;

public class Solution {
    /**
     * Given a string array `words`, return _an array of all characters that show up
     * in all strings within the_`words` _(including duplicates)_. You may return the
     * answer in **any order**.
     *
     * @param words a string array
     * @return an array of all characters that show up in all strings within the `words` (including duplicates)
     */
    public List<String> commonChars(String[] words) {
        if (words == null || words.length == 0) {
            return new ArrayList<>();
        }
        
        Map<Character, Integer> commonCount = new HashMap<>();
        Map<Character, Integer> wordCount;
        
        for (String word : words) {
            wordCount = new HashMap<>();
            for (char ch : word.toCharArray()) {
                wordCount.put(ch, wordCount.getOrDefault(ch, 0) + 1);
            }
            
            if (commonCount.isEmpty()) {
                commonCount = wordCount;
            } else {
                for (Map.Entry<Character, Integer> entry : commonCount.entrySet()) {
                    commonCount.put(entry.getKey(), Math.min(commonCount.get(entry.getKey()), wordCount.getOrDefault(entry.getKey(), 0)));
                }
            }
        }
        
        List<String> result = new ArrayList<>();
        for (Map.Entry<Character, Integer> entry : commonCount.entrySet()) {
            for (int i = 0; i < entry.getValue(); i++) {
                result.add(String.valueOf(entry.getKey()));
            }
        }
        
        return result;
    }
}