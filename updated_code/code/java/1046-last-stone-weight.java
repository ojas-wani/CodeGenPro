package com.example;

import java.util.PriorityQueue;

/**
 * Solution for the Last Stone Weight problem.
 *
 * @author Your Name
 */
public class Solution {
    /**
     * Returns the weight of the last remaining stone.
     *
     * @param stones the weights of the stones
     * @return the weight of the last remaining stone, or 0 if there are no stones left
     */
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((x, y) -> y - x);
        for (int stone : stones) {
            pq.add(stone);
        }

        while (pq.size() > 1) {
            int y = pq.poll();
            int x = pq.poll();
            if (x != y) {
                pq.add(y - x);
            }
        }

        return pq.isEmpty() ? 0 : pq.peek();
    }
}