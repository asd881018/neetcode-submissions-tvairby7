class Solution {
    public int[] twoSum(int[] nums, int target) {
        int length = nums.length;
        HashMap <Integer, Integer> prevMap = new HashMap<>();

        // nums[i] + nums[j] == target
        // nums[j] = target - nums[i];
        // diff = target - nums[i];
        for (int i = 0; i < length; i++) {
            int diff = target - nums[i];
            int num = nums[i];

            if (prevMap.containsKey(diff)) {
                return new int[]{prevMap.get(diff), i};
            }
            else {
                prevMap.put(nums[i], i);
            }
        }
        return new int[]{};
    }
}
