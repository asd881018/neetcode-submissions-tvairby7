class Solution {
    public boolean isValid(String s) {

        int len = s.length();

        if (len == 0) {
            return true;
        }

        if (len % 2 != 0) {
            return false;
        }
        
        // Use a stack
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) { // Use char instead of Character
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                char openBracket = stack.pop();
                char closeBracket = c;
                if (openBracket == '(' && closeBracket != ')') {
                    return false;
                } else if (openBracket == '[' && closeBracket != ']') {
                    return false;
                } else if (openBracket == '{' && closeBracket != '}') {
                    return false;
                }
            }
        }

        return stack.isEmpty(); // Simplified return statement
    }
}
