package com.example;

import java.util.Arrays;

public class Solution {
    /**
     * A newly designed keypad was tested, where a tester pressed a sequence of `n`
     * keys, one at a time.
     * 
     * @param releaseTimes a sorted list where `releaseTimes[i]` was the time the
     *            `ith` key was released.
     * @param keysPressed a string of length `n`, where `keysPressed[i]` was the
     *            `ith` key pressed in the testing sequence.
     * @return the key of the keypress that had the longest duration. If there are
     *         multiple such keypresses, return the lexicographically largest key
     *         of the keypresses.
     */
    public char slowestKey(int[] releaseTimes, String keysPressed) {
        int maxDuration = releaseTimes[0];
        char slowestKey = keysPressed.charAt(0);
        for (int i = 1; i < releaseTimes.length; i++) {
            final int duration = releaseTimes[i] - releaseTimes[i - 1];
            if (duration > maxDuration || (duration == maxDuration && keysPressed.charAt(i) > slowestKey)) {
                maxDuration = duration;
                slowestKey = keysPressed.charAt(i);
            }
        }
        return slowestKey;
    }
}