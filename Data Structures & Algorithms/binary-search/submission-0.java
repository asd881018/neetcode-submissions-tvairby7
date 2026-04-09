class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        int m;

        while (l <= r) {
            if (nums[l] == target) {
                return l;
            }
            if (nums[r] == target) {
                return r;
            }
            m = (l + r) / 2;
            if (nums[m] == target) {
                return m;
            } else if (nums[m] <= target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return -1;
    }
}
