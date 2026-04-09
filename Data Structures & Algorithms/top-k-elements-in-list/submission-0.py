class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        # store the count in the hashmap
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # append the the most freq num into res for k times

        arr = []

        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res