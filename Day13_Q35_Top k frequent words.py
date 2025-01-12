class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}

        for word in words:
            if word  in d:
                d[word] +=1
            elif word not in d:
                d[word] = 1

        l = sorted(d.items(),key = lambda x: (-x[1],x[0]))
    
        return [item[0] for item in l[:k]]