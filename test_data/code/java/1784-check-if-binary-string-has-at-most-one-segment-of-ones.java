class Solution {
    public boolean checkOnesSegment(String s) {
        int count = 0;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '1'){
                if(count == 0){
                    count++;
                }else{
                    return false;
                }
            }
        }
        return true;
    }
}