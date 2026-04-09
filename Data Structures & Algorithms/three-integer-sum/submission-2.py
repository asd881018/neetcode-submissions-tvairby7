class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # [-1,0,1,2,-1,-4]

        # 1. brute force: 
        # for i
        #   for j
        #       for k
        # find nums[i] + nums[j] + nums[k] == 0

        # 2.
        # [-4,-1,-1,0,1,2]

        # nums[i] = -(nums[j] + nums[k])
        # target =-nums[i] = nums[j] + nums[k] 
        # Find nums[j] + nums[k] in >=0 numbers
        # pointer, j from left (i + 1), k from right (len-1)
        # while j<k:
        # if nums[j] + nums[k] == target
        # append to res
        # elif nums[j] + nums[k] > target
        # j++
        # else
        # k--

        nums.sort()
        res = []

        length = len(nums)
        for i in range(length):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, length - 1

            while j < k:
                threeSum = nums[i] + nums[j] + nums[k] 
                if threeSum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif threeSum < 0:
                    j += 1
                else:
                    k -= 1
                    

        return res

