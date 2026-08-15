class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        #  Brute Force 

        # flag = False
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]==nums[j]:
        #             flag = True
        # return flag

        freq_map = {}

        flag = False

        for i in range(n):
            freq_map[nums[i]] = freq_map.get(nums[i],0)+1
        
        for key, value in freq_map.items():
            if value > 1:
                flag = True
        return flag
        

