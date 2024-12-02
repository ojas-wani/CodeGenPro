import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        ArrayList<int[]> list = new ArrayList<>();
        
        for(int i = 0; i < mat.length; i++){
            int count = 0;
            for(int j = 0; j < mat[i].length; j++){
                if(mat[i][j] == 1) count++;
            }
            list.add(new int[]{count, i});
        }
        
        list.sort((a, b) -> a[0] - b[0] == 0 ? a[1] - b[1] : a[0] - b[0]);
        
        int[] result = new int[k];
        for(int i = 0; i < k; i++){
            result[i] = list.get(i)[1] + 1;
        }
        
        return result;
    }
}