class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        res = ""
        b = 0
        c = 0
        guess = list(guess)
        secret = list(secret)
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                b+=1
                guess[i] = '_'
                secret[i] = '_'

        for i in range(len(guess)):
            if guess[i]!= '_' and guess[i] in secret:
                c+=1
                secret[secret.index(guess[i])] = '_'

        

        
        res = f"{b}A{c}B"
        return res


        