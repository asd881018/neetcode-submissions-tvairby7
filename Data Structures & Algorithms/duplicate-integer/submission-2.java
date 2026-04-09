class Solution {
    public boolean hasDuplicate(int[] nums) {
        // int nums_length = nums.length;
        // // 1. Using nested for loop to check, O(n^2)
        // for (int i = 0; i < nums_length; i++){
        //     for (int j = i + 1; j < nums_length; j++){
        //         if (nums[i]==nums[j])
        //             return true;
        //     }
        // }
        // return false;

        // // 2. Create a HashSet O(n)
        // Set<Integer> uniques = new HashSet<>();
        // for (int i = 0; i < nums_length; i++){
        //     if (uniques.contains(nums[i]))
        //         return true;
        //     uniques.add(nums[i]);
        // }
        // return false;






        // 1. Brute force , use two for loop to find if nums[i] == nums[j]
        // 2. Using HashSet/HashMap, to record the int in the nums. then check if it has duplicate int

        HashSet <Integer> prevSet = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (prevSet.contains(num)) {
                return true;
            } else {
                prevSet.add(num);
            }
        }
        return false;
    }
}
