class Solution {
    public int maxProfit(int[] prices) {
        
        // int maxProfit = 0;
        // int len = prices.length;
        // int profit = 0; 
        // // 1. Use nested loop to find the max positive diff
        // for (int i = 0; i < len; i++){
        //     for (int j = i + 1; j < len; j++){
        //         profit = prices[j] - prices[i];
        //         if (profit > maxProfit){
        //             maxProfit = profit;
        //         }
        //     }
        // }
        // return maxProfit;


        // 2. Two Pointers
        // int left = 0; 
        // int right = 1;
        // int maxProfit = 0;
        // while (right < prices.length){
        //     if (prices[left] < prices[right]){
        //         maxProfit = Math.max(maxProfit, prices[right] - prices[left]);
        //     } else {
        //         left = right;
        //     }
        //     right++;
        // }
        // return maxProfit;

        // 1. Brute Force, two for loop

        // 2. Two Pointer
        int length = prices.length; 
        int l = 0;
        int r = 1;
        int max = 0;

        while (r < length) {
            if (prices[l] < prices[r]) {
                max = Math.max(max, prices[r] - prices[l]);
            } else {
                l = r;
            }
            r++;
        }
        return max;
    }
}
