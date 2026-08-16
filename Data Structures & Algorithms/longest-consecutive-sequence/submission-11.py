class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

# Optimal Solution

        n = len(nums)
        my_set = set(nums)

        maximum = 0

        for num in nums:
            if num-1 not in my_set:
                x = num
                count=1
                while x+1 in my_set:
                    count+=1
                    x+=1
                maximum = max(maximum,count)

        return maximum

# Brute force
        # n = len(nums)
        # if n == 0: return 0
        # nums.sort()
        # maxi = 1
        # count = 1

        # for i in range(n-1):
        #     if nums[i+1]-nums[i]==1:
        #         count+=1
        #         maxi = max(maxi,count)
        #     elif nums[i+1]==nums[i]:
        #         continue
        #     else:
        #         count = 1
        # return maxi