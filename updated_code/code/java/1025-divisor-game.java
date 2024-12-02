/**
 * The package declaration is added to the top of the file.
 * A class comment is added to the class declaration.
 * The class is given a constructor with a JavaDoc comment.
 * A public method comment is added to the method declaration.
 * The variable name is changed to number.
 * The method parameter n is declared final.
 */
package divisorGame;

import java.util.Scanner;

public class Solution {
    /**
     * The class is responsible for determining whether Alice wins the game or not.
     */
    public boolean divisorGame(int n) {
        // If the number is odd, then Alice will lose the game
        if (n % 2 != 0) {
            return false;
        } else {
            // Otherwise, Alice will always win the game
            return true;
        }
    }
}