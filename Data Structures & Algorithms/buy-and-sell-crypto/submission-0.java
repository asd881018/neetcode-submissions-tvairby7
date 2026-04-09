class Solution {
    public int maxProfit(int[] prices) {
        
        int maxProfit = 0;
        int len = prices.length;
        int profit = 0; 
        // 1. Use nested loop to find the max positive diff
        for (int i = 0; i < len; i++){
            for (int j = i + 1; j < len; j++){
                profit = prices[j] - prices[i];
                if (profit > maxProfit){
                    maxProfit = profit;
                }
            }
        }
        return maxProfit;
    }
}
