class Solution:
    def isValid(self, s: str) -> bool:

        # Create a Map
        Map = {']':'[', '}' : '{', ')' : '('}
        
        # Have a stack to store all the left brackets
        stack = []
        
        for c in s:
            # store opening bracket
            if c not in Map:
                stack.append(c)
                continue
            # The closing bracket not match the latest openning bracket
            # or the stack is empty
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
        
        # When it has the match right bracket
        # If no, return faslse
        # If yes
        # Remove the left bracket in the stack

        # Return true if stack is empty


