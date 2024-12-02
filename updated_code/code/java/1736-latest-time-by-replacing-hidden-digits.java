package com.leetcode;

import java.util.Arrays;

/**
 * Class comments are required
 */
public class Solution {

    /**
     * Public method and constructor comments are required
     *
     * @param time a string in the form of hh:mm, where some of the digits in the string are hidden (represented by '?')
     * @return the latest valid time you can get from time by replacing the hidden digits
     */
    public String maximumTime(String time) {
        char[] arr = time.toCharArray();

        if (arr[0] == '?') {
            arr[0] = '2';
        }
        if (arr[1] == '?') {
            arr[1] = '3';
        }
        if (arr[3] == '?') {
            arr[3] = '5';
        }
        if (arr[4] == '?') {
            arr[4] = '9';
        }

        return new String(arr);
    }
}