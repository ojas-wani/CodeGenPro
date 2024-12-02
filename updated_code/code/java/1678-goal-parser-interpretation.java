package orggoals.parser;

import java.utilStringBuilder;

public class GoalParser {

    public String interpret(String command) {
        StringBuilder res = new StringBuilder();
        for(int i = 0; i < command.length(); i++) {
            if(command.charAt(i) == 'G') {
                res.append('G');
            } else if(command.charAt(i) == '(') {
                int j = i + 1;
                while(j < command.length() && command.charAt(j) != ')') {
                    j++;
                }
                if(j < command.length() && command.substring(i, j + 1).equals("(al)")) {
                    res.append("al");
                    i = j;
                } else {
                    res.append('o');
                }
            }
        }
        return res.toString();
    }
}