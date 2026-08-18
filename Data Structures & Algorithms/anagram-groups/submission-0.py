class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti = {}

        for str in strs:
            freqArray = [0] * 27
            for char in str:
               freqArray[ord(char) - ord('a')] += 1
            freqArray = tuple(freqArray)
            if freqArray in dicti:
                dicti[freqArray].append(str)
            else:
                dicti[freqArray] = [str]

        return list(dicti.values())