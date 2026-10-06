class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # myDict = {}
        # for ch_s in s:
        #     if ch_s not in myDict.keys():
        #         myDict.setdefault(ch_s, 1)
        #     else:
        #         myDict[ch_s] += 1
        # for ch_t in t:
        #     if ch_t in myDict.keys():
        #         myDict[ch_t] -= 1
        #     else:
        #         return False
        
        # for value in myDict.values():
        #     if value != 0:
        #         return False

        # return True
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT

        

        