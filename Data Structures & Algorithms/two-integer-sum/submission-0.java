class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] pair = new int[2];
        int length = nums.length;
        // 1. Brute Force, nested for loop, O(n^2)
        for (int i = 0; i < length; i++)
            for (int j = i + 1; j < length; j++){
                if (nums[i] + nums[j] == target){
                    pair[0] = i;
                    pair[1] = j;
                    return pair;
                }
            }
            
        return new int[0];
    }
}
