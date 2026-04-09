class Solution {
    public int climbStairs(int n) {
        
    //     int one = 1;
    //     int two = 1;

    //     for (int i = 0; i < n -1; i++) {
    //         int temp = one;
    //         one = one + two;
    //         two = temp;
    //     }
    //     return one;
    // }







        // n = 1 -> 1
        //  1 

        // n = 2 -> 2
        //  1 + 1
        //  2

        // n = 3 -> 3
        // 111
        // 12
        // 2 1

        // n = 4 -> 5
        // 1111
        // 112
        // 121
        // 211
        // 22

        // n = 5 -> 8
        // 11111 
        // 1112 
        // 122 

        // n = 5 = f(4) + f(3)
        // f(n) = f(n-1) + f(n-2)

        if (n == 1) {return 1;};
        if (n == 2) {return 2;};

        return climbStairs(n - 1) + climbStairs(n - 2);

        
    }
}
