class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        r = []
        while columnNumber>0:
            columnNumber -= 1
            c = chr(columnNumber%26 + ord('A'))
            r.append(c)
            columnNumber //= 26
        return ''.join(r[::-1])
        