class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num,0)+1
        sorted_freq = sorted(freq_map.items(), key=lambda item : item[1], reverse = True)

        result = []

        for i in range(k):
            result.append(sorted_freq[i][0])
        return result