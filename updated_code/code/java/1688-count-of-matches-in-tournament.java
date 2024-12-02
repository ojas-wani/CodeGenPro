package tournamentmatches;
import java.util.Scanner;

/**
 * This class calculates the number of matches in a tournament.
 * 
 * @author Your Name
 * @version 1.0
 */

public class Solution {
    /**
     * This method calculates the number of matches in a tournament.
     * 
     * @param n The number of teams in the tournament.
     * @return The number of matches played in the tournament.
     */

    public int numberOfMatches(int n) {
        int totalMatches = 0;
        int remainingTeams = n;

        while (remainingTeams > 1) {
            if (remainingTeams % 2 == 0) {
                totalMatches += remainingTeams / 2;
                remainingTeams = remainingTeams / 2;
            } else {
                totalMatches += (remainingTeams - 1) / 2;
                remainingTeams = (remainingTeams - 1) / 2 + 1;
            }
        }
        return totalMatches;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();
        Solution solution = new Solution();
        System.out.println(solution.numberOfMatches(n));
    }
}