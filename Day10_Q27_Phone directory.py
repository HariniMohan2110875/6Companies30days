#User function Template for python3

class Solution:
    def displayContacts(self, n, contact, s):
        # code here
        contact = sorted(set(contact))
        res = []
        p = ""        
        for c in s:
            p+=c
            matches = [m for m in contact if m.startswith(p)]
            if matches:
                res.append(matches)
            else:
                res.append(["0"])
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        contact = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.displayContacts(n, contact, s)
        for i in range(len(s)):
            for val in ans[i]:
                print(val, end = " ")
            print()
        print("~")
# } Driver Code Ends