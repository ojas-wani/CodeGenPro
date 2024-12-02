class Solution {
    public String sortString(String s) {
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        
        StringBuilder sb = new StringBuilder();
        int i = 0, j = arr.length - 1;
        
        while (i <= j) {
            if (arr[i] <= arr[j]) {
                sb.append(arr[i++]);
                if (i <= j) {
                    sb.append(arr[i--]);
                }
            } else {
                sb.append(arr[j--]);
                if (i <= j) {
                    sb.append(arr[i++]);
                }
            }
        }
        
        return sb.toString();
    }
}