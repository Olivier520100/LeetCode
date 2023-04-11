class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        strlastindex = len(strx)-1
        i = 0
        j = strlastindex
        palinbool = True
        while j >= i and palinbool == True:
            if strx[i] != strx[j]:
                palinbool = False
            i+=1
            j-=1
            
        print(palinbool)
        return palinbool
            