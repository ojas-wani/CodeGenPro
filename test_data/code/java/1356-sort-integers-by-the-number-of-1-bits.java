class Solution {
    public int[] sortByBits(int[] arr) {
        int[] result = new int[arr.length];
        for(int i = 0; i < arr.length; i++){
            result[i] = arr[i];
        }
        Arrays.sort(result, (a, b) -> {
            int oneCountA = Integer.bitCount(a);
            int oneCountB = Integer.bitCount(b);
            if(oneCountA != oneCountB){
                return Integer.compare(oneCountA, oneCountB);
            }else{
                return Integer.compare(a, b);
            }
        });
        return result;
    }
}