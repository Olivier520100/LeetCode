class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        dict1 = {s[0]:"1"}
        dict2 = {t[0]:"1"}


        i = 1
        sstring ="1"
        tstring ="1"
        spointer = 2
        tpointer = 2
        while (i < len(s)):
            if s[i] in dict1:
                k = 0
            else:
                dict1[s[i]] = str(spointer)
                spointer+=1
            if t[i] in dict2:
                k = 0
            else:
                dict2[t[i]] = str(tpointer)
                tpointer+=1
            sstring+=dict1[s[i]]
            tstring+=dict2[t[i]]

            i+=1

        if (sstring == tstring):
            return True
        else:
            return False

