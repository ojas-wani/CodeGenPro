import java.util.*;

public class Solution {
    /**
     * Given an array of string `words`, return _all strings in_`words` _that is a
     * **substring** of another word_. You can return the answer in **any order**.
     *
     * @param words an array of string
     * @return all strings in `words` that is a substring of another word
     */
    public List<String> stringMatching(String[] words) {
        List<String> result = new ArrayList<>();
        for (String word1 : words) {
            for (String word2 : words) {
                if (word1.equals(word2)) {
                    continue;
                }
                if (word2.indexOf(word1) != -1) {
                    result.add(word1);
                    break;
                }
            }
        }
        return result;
    }
}