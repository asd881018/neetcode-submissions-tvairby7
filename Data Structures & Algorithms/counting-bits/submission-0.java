class Solution {
    public int[] countBits(int n) {
        
        // 1. using a for loop to generate a list from 1 to n
        // Convert the elements to binary
        // Counting the 1 of each elements:
        //      while n not equl 0:
        //          count+ = n % 2;
        //          n = n >>> 2;
        // O (n logn)

        // 0 0000
        // 1 0001 -> 1 + dp[n-1]
        // 2 0010 -> 1 + dp[n-2]
        // 3 0011
        // 4 0100

        // 5 0101 -> 1 + dp[n-4]
        // 6 0110
        // 7 0111
        // 8 1000 -> 1 + dp[n-8]

        // offset = 1, 2, 4, 8 ,16

        int[] dp = new int [n + 1];
        int offset = 1;

        for (int i = 1; i <= n; i++) {
            if (offset * 2 == i){
                offset = i;
            }
            dp[i] = 1 + dp[i - offset];
        }
        return dp;
    }
}
