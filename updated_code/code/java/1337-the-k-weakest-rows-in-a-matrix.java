/*
 * @author <your_name>
 * @since <date>
 */
package <your_package>;

import java.util.*;

public class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        List<int[]> list = new ArrayList<>();
        
        for (int i = 0; i < mat.length; i++) {
            int count = 0;
            for (int j = 0; j < mat[i].length; j++) {
                if (mat[i][j] == 1) {
                    count++;
                }
            }
            list.add(new int[]{count, i});
        }
        
        list.sort(Comparator.comparingInt(a -> a[0]).thenComparingInt(a -> a[1]));
        
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = list.get(i)[1] + 1;
        }
        
        return result;
    }
}