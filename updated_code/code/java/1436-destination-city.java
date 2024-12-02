package com.wwcode;

import java.util.*;

public class Solution {
    /**
     * You are given the array `paths`, where `paths[i] = [cityAi, cityBi]` means
     * there exists a direct path going from `cityAi` to `cityBi`. 
     * _Return the destination city, that is, the city without any path outgoing to another city._
     * 
     * It is guaranteed that the graph of paths forms a line without any loop,
     * therefore, there will be exactly one destination city.
     * 
     * @param paths a list of paths where `paths[i] = [cityAi, cityBi]` means 
     *              there exists a direct path going from `cityAi` to `cityBi`.
     * @return the destination city, that is, the city without any path outgoing to another city.
     */
    public String destCity(List<List<String>> paths) {
        Set<String> cities = new HashSet<>();
        for (List<String> path : paths) {
            cities.add(path.get(0));
            if (!cities.contains(path.get(1))) {
                return path.get(1);
            }
        }
        return "";
    }
}