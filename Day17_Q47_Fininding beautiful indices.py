class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        sl  = len(s)
        al = len(a)
        bl = len(b)

        l = []


        a_indices = [i for i in range(sl - al + 1) if s[i:i+al] == a]

        b_indices = {i for i in range(sl - bl + 1) if s[i:i+bl] == b}

        for i in a_indices:
            for j in b_indices:
                if abs(j - i) <= k:
                    l.append(i)
                    break  

        return sorted(l)
