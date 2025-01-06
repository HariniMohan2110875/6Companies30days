class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] = 0
        print(d) 
        for k,v in d.items():
            if v==1:
                return s.index(k)
        return -1

        