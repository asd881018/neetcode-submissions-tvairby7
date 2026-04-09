class Solution {
    public boolean hasDuplicate(int[] nums) {
        int nums_length = nums.length;
        // 1. Using nested for loop to check, O(n^2)
        // for (int i = 0; i < nums_length; i++){
        //     for (int j = i + 1; j < nums_length; j++){
        //         if (nums[i]==nums[j])
        //             return true;
        //     }
        // }
        // return false;

        // 2. Create a HashSet O(n)
        Set<Integer> uniques = new HashSet<>();
        // Record the number into hashtable if it is not in hastable
        for (int i = 0; i < nums_length; i++){
            if (uniques.contains(nums[i]))
                return true;
            uniques.add(nums[i]);
        }
        return false;
    }
}
