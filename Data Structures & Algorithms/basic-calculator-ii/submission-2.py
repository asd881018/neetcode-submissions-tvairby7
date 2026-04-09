class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []

        i = 0

        while i < len(s):

            cur = s[i]

            if cur == ' ':
                i += 1
                continue

            if cur.isdigit():

                num = int(cur)
                
                while i + 1 < len(s) and s[i+1].isdigit() :
                    i += 1
                    num = num * 10 + int(s[i]) 

                if stack and stack[-1] in ('*', '/'):
                    op = stack.pop()
                    prev = stack.pop()

                    if op == '*':
                        stack.append(prev * num)
                    else:
                        stack.append(prev // num)
                else:
                    stack.append(num)
                
            else:
                stack.append(cur)
            i += 1

        res = stack.pop(0)
        i = 0

        while i < len(stack):
            op = stack[i]
            num = stack[i+1]

            if op == '+':
                res += num
            else:
                res -= num

            i += 2

        return res