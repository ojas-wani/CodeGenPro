class Solution {
    public int bitwiseComplement(int n) {
        int temp = n, sum = 0, keep = 1;
        while (temp > 0) {
            temp = temp >> 1;
            sum = sum + keep * (1 & (n ^ temp));
            keep *= 2;
        }
        return sum;
    }
}