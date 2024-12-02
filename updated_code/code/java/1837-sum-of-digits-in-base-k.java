package llmImprovedCodeQuality.testData.temp2.code.java;

import java.util.Scanner;

/**
 * This class defines a method to calculate the sum of digits of a number after converting it to a new base.
 */
public class SumOfDigitsInBaseK {
    /**
     * Calculate the sum of digits of a number after converting it to a new base.
     * 
     * @param n the number to be converted and summed
     * @param k the base to convert the number to
     * @return the sum of digits in the new base
     */
    public int sumBase(int n, final int k) {
        int sum = 0;
        while (n > 0) {
            n = n % k;
            sum = sum + n;
            n = n / k;
        }
        return sum;
    }

    public static void main(String[] args) {
        SumOfDigitsInBaseK sumOfDigitsInBaseK = new SumOfDigitsInBaseK();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number:");
        int n = scanner.nextInt();
        System.out.println("Enter the base:");
        int k = scanner.nextInt();
        int result = sumOfDigitsInBaseK.sumBase(n, k);
        System.out.println("The sum of digits in base " + k + " is: " + result);
    }
}