class Solution {
    public int romanToInt(String s) {
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(i < s.length() - 1){
                char c2 = s.charAt(i+1);
                if((c == 'I' && (c2 == 'V' || c2 == 'X')) ||
                (c == 'X' && (c2 == 'L' || c2 == 'C')) ||
                (c == 'C' && (c2 == 'D' || c2 == 'M'))){
                    sum -= getNumber(c);
                }else{
                    sum += getNumber(c);
                }
            }else{
                sum += getNumber(c);
            }
        }
        return sum;
    }
    private int getNumber(char c){
        if(c == 'I') return 1;
        if(c == 'V') return 5;
        if(c == 'X') return 10;
        if(c == 'L') return 50;
        if(c == 'C') return 100;
        if(c == 'D') return 500;
        if(c == 'M') return 1000;
        return 0;
    }
}