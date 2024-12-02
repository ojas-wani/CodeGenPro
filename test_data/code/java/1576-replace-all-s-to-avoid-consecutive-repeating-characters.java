class Solution {
    public String modifyString(String s) {
        char[] arr = s.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == '?') {
                int left = i - 1, right = i + 1;
                char temp = '?';
                while (left >= 0 && arr[left] == temp) {
                    left--;
                }
                while (right < arr.length && arr[right] == temp) {
                    right++;
                }
                if (left >= 0) {
                    temp = (char) (left < 0 ? 'a' : arr[left]);
                } else {
                    temp = 'a';
                }
                arr[i] = (char) (right == arr.length ? 'z' : arr[right]);
                if (temp == arr[i]) {
                    temp = (char) (temp + 1);
                }
                arr[i] = (char) (temp > 'a' ? temp - 1 : temp);
            }
        }
        return new String(arr);
    }
}