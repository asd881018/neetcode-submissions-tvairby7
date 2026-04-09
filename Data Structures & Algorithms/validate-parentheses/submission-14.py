class Solution:
    def isValid(self, s: str) -> bool:
        bStack = []
        bMap = {']':'[', ')':'(', '}':'{'}
        for c in s:
            # open bracket , push to stack
            if c not in bMap:
                bStack.append(c)
            # close bracket, if the pop from stack not match return False 
            else:
                if not bStack or bStack.pop() != bMap[c]:
                    return False
        return True if not bStack else False

        