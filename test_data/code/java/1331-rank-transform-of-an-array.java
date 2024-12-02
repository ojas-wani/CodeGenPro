class Solution {
    public int[] arrayRankTransform(int[] arr) {
        Arrays.sort(arr);
        Map<Integer, Integer> rankMap = new HashMap<>();
        rankMap.put(arr[0], 1);
        int currentRank = 1;

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] != arr[i - 1]) {
                currentRank++;
            }
            rankMap.put(arr[i], currentRank);
        }

        int[] result = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            result[i] = rankMap.get(arr[i]);
        }
        return result;
    }
}