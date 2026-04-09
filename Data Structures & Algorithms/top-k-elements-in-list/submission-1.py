class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store the occurance of num into hashmap
        # sort the hashmap with hashmap's value
        # for i in range(k):
            # pop the most occurance of num from hashmap
            # store in res[]
        # return res

        res = []
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])
        return res