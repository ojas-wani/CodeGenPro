class Solution {
    public int findLucky(int[] arr) {
        Map<Integer, Integer> frequency = new HashMap<>();
        for (int num : arr) {
            frequency.put(num, frequency.getOrDefault(num, 0) + 1);
        }
        
        int result = -1;
        for (Map.Entry<Integer, Integer> entry : frequency.entrySet()) {
            if (entry.getKey() == entry.getValue()) {
                result = Math.max(result, entry.getKey());
            }
        }
        return result;
    }
}