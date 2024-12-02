import java.util.Random;

public class Solution {
    private final Random random = new Random();

    /**
     * Given a string `s` containing only lowercase English letters and the `'?'`
     * character, convert **all** the `'?'` characters into lowercase letters such
     * that the final string does not contain any **consecutive repeating**
     * characters. You **cannot** modify the non `'?'` characters.
     *
     * @param s the input string
     * @return the final string after all the conversions (possibly zero) have been made
     */
    public String modifyString(String s) {
        char[] arr = s.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == '?') {
                int left = i - 1;
                int right = i + 1;
                while (left >= 0 && arr[left] == 'z') {
                    left--;
                }
                while (right < arr.length && arr[right] == 'a') {
                    right++;
                }
                if (left >= 0) {
                    arr[i] = (char) ('a' + random.nextInt('z' - 'a'));
                } else {
                    arr[i] = 'a';
                }
                if (right < arr.length) {
                    arr[i] = (char) (arr[right] - (arr[right] == 'z' ? 1 : 0));
                } else {
                    arr[i] = 'z';
                }
            }
        }
        return new String(arr);
    }
}