import java.util.PriorityQueue;

class Solution {
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