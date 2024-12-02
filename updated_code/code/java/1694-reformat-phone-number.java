package com.reformatnumber;

import java.util.ArrayList;
import java.util.List;

public class Solution {

    /**
     * Reformat the phone number in a certain manner.
     *
     * @param number the phone number as a string
     * @return the phone number after formatting
     */
    public String reformatNumber(String number) {
        number = number.replaceAll("[^0-9]", "");
        StringBuilder sb = new StringBuilder();
        List<String> blocks = new ArrayList<>();
        int n = number.length();
        for (int i = 0; i < n; i += 3) {
            String block = number.substring(i, Math.min(i + 3, n));
            if (block.length() == 1) {
                if (blocks.size() > 0) {
                    blocks.add(block);
                } else {
                    // The first block cannot be a single digit
                    throw new RuntimeException("Invalid phone number");
                }
            } else if (block.length() == 2) {
                // We want at most two blocks of length 2
                if (blocks.size() > 1) {
                    throw new RuntimeException("Invalid phone number");
                }
                blocks.add(block);
            } else {
                blocks.add(block);
            }
        }
        for (String block : blocks) {
            sb.append(block);
            if (!blocks.equals(blocks.get(blocks.size() - 1))) {
                sb.append("-");
            }
        }
        return sb.toString();
    }
}