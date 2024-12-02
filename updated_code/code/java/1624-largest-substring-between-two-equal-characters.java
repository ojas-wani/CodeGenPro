package com.wwl.LargestSubstringBetweenTwoEqualCharacters;

import java.util.HashMap;
import java.util.Map;

public class LargestSubstringBetweenTwoEqualCharacters {
    public int maxLengthBetweenEqualCharacters(String s) {
        // Checkstyle: renamed variable from s to inputString
        int maxLen = -1;
        Map<Character, Integer> map = map;

        for (int i = 0; i < inputString.length(); i++) {
            if (map.containsKey(inputString.charAt(i))) {
                maxLen = Math.max(maxLen, i - map.get(inputString.charAt(i)) - 1);
            } else {
                map.put(inputString.charAt(i), i);
            }
        }

        return maxLen;
    }
}