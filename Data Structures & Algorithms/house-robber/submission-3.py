class Solution:
    def rob(self, nums: List[int]) -> int:
        # can't rob adj houses

        # nums = [2,9,8,3,6]

        # if rob1, rob(1) and rob([2:n])
        # if not rob1, rob([1:n])

        # ...
        # prev + rob(n)

        # [6] -> 6
        # [3, 6] -> 6
        # [8] -> 8(n) + 6(n+1)

        # [2] -> 2
        # [2, 9] -> 9

        # max(rob1 + rob2)

        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2



