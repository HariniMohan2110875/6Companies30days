class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        l = []
        seen = {}

        for i in range(n-9):
            subs = s[i:i+10]

            print(subs)

            if subs in seen:
                if seen[subs] == 1:
                    l.append(subs)
                seen[subs] +=1
            else:
                seen[subs] = 1
        return l

        