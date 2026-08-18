class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(0,len(nums)):
            dif = target-nums[i]
            if dif in dict:
                return [dict[dif],i]
            dict[nums[i]] = i
        return [0,1]