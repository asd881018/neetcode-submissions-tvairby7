class Solution:
    def climbStairs(self, n: int) -> int:
        
        # n0 = 1
        # n1 = 1
        # n2 = 2
        # n3 = 3
        # n4 = 5
        # n5 = 8

        if n == 1 or n == 0:
            return 1
        if n == 2:
            return 2
        
        # f(n) = f(n-1) + f(n-2)
        return self.climbStairs(n-1) + self.climbStairs(n-2)