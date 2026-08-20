class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        dictL = {}
        maxL = 0
        for c in s:
            #print(dictL)
            while c in dictL:
                dictL.pop(s[l])
                l += 1
            r += 1
            dictL[c] = True
            if maxL < r - l + 1:
                maxL = r - l
        return maxL
