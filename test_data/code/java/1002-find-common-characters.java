import java.util.*;

class Solution {
    public List<String> commonChars(String[] words) {
        Map<Character, Integer> commonCount = new HashMap<>();
        for (String word : words) {
            Map<Character, Integer> count = new HashMap<>();
            for (char ch : word.toCharArray()) {
                count.put(ch, count.getOrDefault(ch, 0) + 1);
            }
            if (commonCount.isEmpty()) {
                commonCount = count;
            } else {
                for (Map.Entry<Character, Integer> entry : commonCount.entrySet()) {
                    commonCount.put(entry.getKey(), Math.min(commonCount.get(entry.getKey()), count.getOrDefault(entry.getKey(), 0)));
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