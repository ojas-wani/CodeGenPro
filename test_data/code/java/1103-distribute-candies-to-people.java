class Solution {
    public int[] distributeCandies(int candies, int num_people) {
        int[] ans = new int[num_people];
        int person = 0;
        int given = 0;

        while (candies > 0) {
            int toGive = Math.min(candies, person + 1);
            ans[person] += toGive;
            candies -= toGive;
            person = (person + 1) % num_people;
        }
        return ans;
    }
}