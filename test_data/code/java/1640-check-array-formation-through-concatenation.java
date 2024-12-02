class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        for (int[] piece : pieces) {
            boolean formed = true;
            int i = 0;
            while (i < arr.length) {
                if (formed) {
                    if (i + piece.length > arr.length) {
                        return false;
                    }
                    boolean match = true;
                    for (int j = 0; j < piece.length; j++) {
                        if (arr[i + j] != piece[j]) {
                            match = false;
                            break;
                        }
                    }
                    if (!match) {
                        return false;
                    }
                }
                i += piece.length;
            }
        }
        return true;
    }
}