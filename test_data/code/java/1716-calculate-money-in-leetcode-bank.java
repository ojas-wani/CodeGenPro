class Solution {
    public int totalMoney(int n) {
        int weeks = n / 7;
        int remainDays = n % 7;
        int total = 0;
        
        for (int i = 1; i <= weeks; i++) {
            total += 28 + i; // 28 = 7 * 4 (1 + 2 + ... + 7)
        }
        
        for (int i = 1; i <= remainDays; i++) {
            total += i + 7; // on the first monday after weeks, he will start from 7
        }
        
        return total;
    }
}