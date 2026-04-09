class Solution {
    public int singleNumber(int[] nums) {
        // Thinking the elements in nums are bitwise
        int res = 0;

        for (int num : nums) {
            res = res ^ num;
        }

        return res;

    }
}
