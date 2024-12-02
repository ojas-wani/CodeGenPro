class Solution {
    public List<Integer> luckyNumbers (int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        List<Integer> result = new ArrayList<>();
        for(int i = 0; i < m; i++){
            int min = matrix[i][0];
            int minCol = 0;
            for(int j = 0; j < n; j++){
                if(matrix[i][j] < min){
                    min = matrix[i][j];
                    minCol = j;
                }
            }
            int maxRow = matrix[0][0];
            for(int j = 0; j < n; j++){
                if(matrix[0][j] > maxRow){
                    maxRow = matrix[0][j];
                }
            }
            if(matrix[i][minCol] == maxRow){
                result.add(matrix[i][minCol]);
            }
        }
        return result;
    }
}