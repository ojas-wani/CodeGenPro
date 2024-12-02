import java.util.Arrays;

public class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        int studentsPointer = 0;
        int sandwichPointer = 0;

        while (studentsPointer < students.length && sandwichPointer < sandwiches.length) {
            if (students[studentsPointer] == sandwiches[sandwichPointer]) {
                studentsPointer++;
                sandwichPointer++;
            } else {
                while (sandwichPointer < sandwiches.length && students[studentsPointer] != sandwiches[sandwichPointer]) {
                    sandwichPointer++;
                }
                if (sandwichPointer == sandwiches.length) {
                    break;
                }
                studentsPointer++;
            }
        }

        return students.length - studentsPointer;
    }
}