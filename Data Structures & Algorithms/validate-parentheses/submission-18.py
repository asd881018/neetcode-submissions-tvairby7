class Solution:
    def isValid(self, s: str) -> bool:
        
        # if open bracket, store into the stack
        # if close bracket, pop the latest element in the stack and aee if it is the coreeslonding open bracket

        # check if the stack is empty or not

        stack = []
        open_brackets = ['(', '{', '[']
        bracket_map = {'}':'{', ')':'(', ']':'['}

        for c in s:

            # if s[i] in open_brackets: 
            #     stack.append(s[i])
            # else:
            #     if not stack:
            #         return False
            #     open_bracket = stack.pop()
            #     if bracket_map[s[i]] != open_bracket:
            #         return False
            if c in bracket_map:
                if stack and bracket_map[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
          return True
        return False 