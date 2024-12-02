class Solution {
    public String maximumTime(String time) {
        char[] arr = time.toCharArray();
        int i = 0;
        if (arr[i] == '?') {
            arr[i] = '2';
        } else {
            i++;
        }
        if (i < 2 && arr[i] == '?') {
            arr[i] = '3';
        } else if (i < 2 && arr[i] != ':') {
            i++;
        }
        if (arr[3] == '?') {
            arr[3] = '5';
        }
        if (arr[4] == '?') {
            arr[4] = '9';
        }
        return String.valueOf(arr);
    }
}