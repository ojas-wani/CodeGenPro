class Solution {
    public boolean squareIsWhite(String coordinates) {
        char col = coordinates.charAt(0);
        int row = Integer.parseInt(coordinates.charAt(1) + "");
        return (col - 'a' + row) % 2 == 1;
    }
}