class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        comparison = strs[0]
        pointer = 1
        charpointer = 0
        continuebool = True

        while (pointer < len(strs)):
            print(comparison)
            while (continuebool and charpointer < min(len(strs[pointer]), len(comparison))):
                
                
                if (comparison[charpointer] != strs[pointer][charpointer]):
                    continuebool = False
                else: 
                    charpointer+=1
                
            
            continuebool = True
            comparison = comparison[0:charpointer]
            pointer +=1;
            charpointer = 0
        
        print(comparison)
    
        return comparison