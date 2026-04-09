class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums = [2,9,8,3,6]
        #         2,9,10
        # max(rob1 + n, rob2)

        # if rob 1st, 1st + 3rd... = rob1 + rob[2:n]
        # if not rob 1st, rob[1:n]

        rob1, rob2 = 0, 0

        #[rob1, rob2, n, n + 1 ...]
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2