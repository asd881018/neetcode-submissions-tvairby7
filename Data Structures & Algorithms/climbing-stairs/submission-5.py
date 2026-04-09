class Solution:
    def climbStairs(self, n: int) -> int:
        # For the last step and last 2 step
        # we have only 1 and 1 solution [x,x,x,x,x,x,x,x,1,1]
        # For example if n = 10, [55,34,21,13,8,5,3,2,1,1]
        if n == 0:
            return 1
        if n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)