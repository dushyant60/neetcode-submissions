class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        freq_map = {}

        for i in range(n):
            temp = target-nums[i]
            if temp in freq_map:
                return [freq_map[temp],i]
            freq_map[nums[i]] = i