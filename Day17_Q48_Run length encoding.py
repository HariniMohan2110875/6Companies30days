
class Solution:
    def encode(self, s: str) -> str:
        l = len(s)
        res = []
        i = 0
        while i < l:
            # Append the current character
            res.append(s[i])
            # Count consecutive occurrences of s[i]
            c = 0
            while i + c < l and s[i] == s[i + c]:
                c += 1
            # Append the count if greater than 1
            
            res.append(str(c))
            # Move to the next different character
            i += c
        return ''.join(res)
