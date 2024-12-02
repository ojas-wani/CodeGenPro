import java.util.*;

public class Solution 
{
    public int sumOfUnique(int[] nums) 
    {
        // map to store the frequency of each element
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : nums) 
        {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }

        // initialize the sum
        int sum = 0;

        // add the elements that appear exactly once to the sum
        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) 
        {
            if (entry.getValue() == 1) 
            {
                sum += entry.getKey();
            }
        }

        return sum;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = [1,2,3,2];
        System.out.println(solution.sumOfUnique(nums));
    }
}