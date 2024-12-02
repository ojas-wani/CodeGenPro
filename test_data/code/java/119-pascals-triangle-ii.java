import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<>();
        row.add(1);
        for (int i = 1; i <= rowIndex; i++) {
            row.add(0);
        }
        for (int i = 1; i <= rowIndex; i++) {
            if (i < 2) {
                row.set(i, 1);
            } else {
                row.set(i, row.get(i - 1) + row.get(i - 2));
            }
        }
        return row;
    }
}