package com.example;

import java.util.HashSet;

public class Solution {
    public boolean isPathCrossing(String path) {
        // Check for the description and reports
        int x = 0, y = 0;
        HashSet<String> visited = new HashSet<>();
        visited.add("0,0");
        for (char c : path.toCharArray()) {
            switch (c) {
                case 'N':
                    y++;
                    break;
                case 'S':
                    y--;
                    break;
                case 'E':
                    x++;
                    break;
                case 'W':
                    x--;
                    break;
            }
            String loc = x + "," + y;
            if (visited.contains(loc)) {
                return true;
            }
            visited.add(loc);
        }
        return false;
    }
}