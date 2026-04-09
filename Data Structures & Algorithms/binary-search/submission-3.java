class Solution {
    public int search(int[] nums, int target) {
        // nums is sorted

        int l = 0;
        int r = nums.length - 1;
        int m;
        int num;

        while (l <= r) {
            // m = (l + r) / 2;
            m = l + ((r - l) / 2);
            num = nums[m];
            if (num > target) {
                r = m - 1;
            } else if (num < target) {
                l = m + 1;
            } else {
                return m;
            }
        }

        return -1;
    }
}
