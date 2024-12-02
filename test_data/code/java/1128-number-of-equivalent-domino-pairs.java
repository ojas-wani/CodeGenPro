class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < dominoes.length; i++) {
            String key = Integer.toString(dominoes[i][0]) + "," + Integer.toString(dominoes[i][1]);
            map.put(key, map.getOrDefault(key, 0) + 1);
        }
        int res = 0;
        for (int count : map.values()) {
            res += count * (count - 1) / 2;
        }
        return res;
    }
}