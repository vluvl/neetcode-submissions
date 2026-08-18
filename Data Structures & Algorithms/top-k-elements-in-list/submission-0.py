class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = [[] for i in range(len(nums) + 1)]
        counts = {}

        for num in nums:
            counts[num] = counts.get(num,0) + 1
        for num, cnt in counts.items():
            freqList[cnt].append(num)

        result = []

        for i in range(len(freqList)-1,0,-1):
            for num in freqList[i]:
                result.append(num)
                if len(result) == k:
                    return result