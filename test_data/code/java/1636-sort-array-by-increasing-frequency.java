class Solution {
    public int[] frequencySort(int[] nums) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }
        
        List<Integer> sortedIndices = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            for (int i = 0; i < entry.getValue(); i++) {
                sortedIndices.add(entry.getKey());
            }
        }
        
        Collections.sort(sortedIndices, (a, b) -> {
            if (Collections.frequency(Arrays.asList(nums), a) == Collections.frequency(Arrays.asList(nums), b)) {
                return Integer.compare(b, a);
            } else {
                return Integer.compare(Collections.frequency(Arrays.asList(nums), a), Collections.frequency(Arrays.asList(nums), b));
            }
        });
        
        int[] result = new int[nums.length];
        int index = 0;
        for (int num : sortedIndices) {
            result[index++] = num;
        }
        
        return result;
    }
}