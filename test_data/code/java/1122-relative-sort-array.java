class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < arr1.length; i++) {
            map.put(arr1[i], map.getOrDefault(arr1[i], 0) + 1);
        }
        List<Integer> list = new ArrayList<>();
        for (int num : arr2) {
            while (map.get(num) > 0) {
                list.add(num);
                map.put(num, map.get(num) - 1);
            }
        }
        for (int num : map.keySet()) {
            if (num < arr2[arr2.length - 1]) {
                while (map.get(num) > 0) {
                    list.add(num);
                    map.put(num, map.get(num) - 1);
                }
            } else {
                Collections.sort(map.keySet().stream().filter(n -> n >= arr2[arr2.length - 1]).collect(Collectors.toList()));
                for (int n : map.keySet().stream().filter(n -> n >= arr2[arr2.length - 1]).collect(Collectors.toList())) {
                    while (map.get(n) > 0) {
                        list.add(n);
                        map.put(n, map.get(n) - 1);
                    }
                }
            }
        }
        int[] res = new int[arr1.length];
        for (int i = 0; i < res.length; i++) {
            res[i] = list.get(i);
        }
        return res;
    }
}