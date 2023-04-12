class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer1 = 0
        letternumber = 0
        exitbool = False
        while letternumber < len(s) and pointer1 < len(t):
            
            if s[letternumber] == t[pointer1]:
                print(letternumber)
                print(pointer1)
                letternumber += 1
            pointer1+=1
        if letternumber == len(s): 
            return True
        else: 
            return False
            
