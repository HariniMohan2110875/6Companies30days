class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}

        for l in s:
            if l in d:
                d[l] += 1
            else:
                d[l] = 1
        
        d = dict(sorted(d.items(),key = lambda x: -x[1]))
        res = []
        for key,val in d.items():
            res.append(key*val)
        return "".join(ss for ss in res)

        