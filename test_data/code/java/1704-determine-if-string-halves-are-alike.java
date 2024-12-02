class Solution {
    public boolean halvesAreAlike(String s) {
        int mid = s.length() / 2;
        String half1 = s.substring(0, mid);
        String half2 = s.substring(mid);
        int count1 = 0, count2 = 0;

        for (char c : half1.toCharArray()) {
            if (isVowel(c)) {
                count1++;
            }
        }
        for (char c : half2.toCharArray()) {
            if (isVowel(c)) {
                count2++;
            }
        }

        return count1 == count2;
    }

    private boolean isVowel(char c) {
        c = Character.toLowerCase(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}