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
        Stack<Character> brackets  = new Stack<>();
        Map<Character, Character> bracketLookup = new HashMap<>(3);
        bracketLookup.put(')', '(');
        bracketLookup.put('}', '{');
        bracketLookup.put(']', '[');

        for (char c : s.toCharArray()) { // Use char instead of Character
            if (bracketLookup.containsKey(c)) {
                if (!brackets.isEmpty() && bracketLookup.get(c).equals(brackets.peek())) {
                    brackets.pop();
                } else {
                    return false;
                }
            } else {
                brackets.push(c);
            }
            
        }

        return brackets.isEmpty(); // Simplified return statement
    }
}
