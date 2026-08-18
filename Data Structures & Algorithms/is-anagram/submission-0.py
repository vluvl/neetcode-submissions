class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        dictt = {}
        for l in s:
            if l in dicts:
                dicts[l] = dicts[l] + 1
            else:
                dicts[l] = 1
        for l in t:
            if l in dictt:
                dictt[l] = dictt[l] + 1
            else:
                dictt[l] = 1
        if dicts == dictt:
            return True
        else:
            return False