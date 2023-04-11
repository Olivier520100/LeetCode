class Solution:
    def isValid(self, s: str) -> bool:


        
        i = 0
        returnval = True
        while (i < len(s) and returnval == True):

            
            if s[i] == ")":
                if (i == 0):
                    returnval = False
                else: 
                    if s[i-1] != "(" : 
                        returnval = False
                    else:
                        s = s[:i] + s[i + 1:]
                        s = s[:i-1] + s[i-1+1:]
                        i = -1
            elif s[i] == "}":
                if (i == 0):
                    returnval = False
                    
                else: 
                    if s[i-1] != "{" : 
                        returnval = False
                    else:
                        s = s[:i] + s[i + 1:]
                        s = s[:i-1] + s[i-1+1:]
                        i = -1
            elif s[i] == "]":
                if (i == 0):
                    returnval = False
                else: 
                    if s[i-1] != "[" : 
                        returnval = False
                    else:
                        s = s[:i] + s[i + 1:]
                        s = s[:i-1] + s[i-1+1:]
                        i = -1
            elif i+1 == len(s):
                returnval = False
            
            i+=1

        
    
        return returnval