import java.util.*;

public class Solution {
    /**
     * Returns a boolean array where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids.
     */
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        // Check for empty array
        if (candies.length == 0) {
            return new ArrayList<>();
        }
        
        List<Boolean> result = new ArrayList<>();
        int maxCandies = Arrays.stream(candies).max().getAsInt();
        
        // Loop through each kid
        for (int candy : candies) {
            result.add(candy + extraCandies >= maxCandies);
        }
        
        return result;
    }
}