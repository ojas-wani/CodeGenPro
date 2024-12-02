class Solution {
    public boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
        int sum = 0;
        int target = 0;
        
        for(int i = 0; i < firstWord.length(); i++){
            sum = sum * 10 + (firstWord.charAt(i) - 'a');
        }
        for(int i = 0; i < secondWord.length(); i++){
            sum = sum + (secondWord.charAt(i) - 'a');
        }
        
        for(int i = 0; i < targetWord.length(); i++){
            target = target * 10 + (targetWord.charAt(i) - 'a');
        }
        
        return sum == target;
    }
}