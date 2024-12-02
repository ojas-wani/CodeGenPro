class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        int i = 0;
        while (i < students.length) {
            if (students[i] == sandwiches[0]) {
                sandwiches = ArrayUtils.remove(sandwiches, 0);
                students = ArrayUtils.remove(students, i);
                i--;
            } else {
                i++;
            }
        }
        return students.length;
    }
}

import java.util.Arrays;

class ArrayUtils {
    public static int[] remove(int[] array, int val) {
        List<Integer> list = new ArrayList<Integer>();
        for (int i : array) {
            if (i != val) {
                list.add(i);
            }
        }
        return list.stream().mapToInt(i -> i).toArray();
    }
}