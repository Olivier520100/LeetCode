class Solution:
    def romanToInt(self, s: str) -> int:
        i=0
        value = 0;
        while (i < len(s)):
            if (s[i] == "I"):

                value+=1
                if (i < len(s)-1):
                    if (s[i+1] == "V"):
                        value+=3
                        i+=1
                    elif (s[i+1] == "X"):
                        value +=8
                        i+=1

            elif (s[i] == "V"):

                value+=5
            elif (s[i] == "X"):

                value+=10
                if (i < len(s)-1):

                    if (s[i+1] == "L"):
                        value+=30
                        i+=1
                    elif (s[i+1] == "C"):
                        value +=80
                        i+=1
            elif (s[i] == "L"):

                value+=50
            elif (s[i] == "C"):

                value+=100
                if (i < len(s)-1):

                    if (s[i+1] =="D"):
                        value+=300
                        i+=1
                    elif (s[i+1] == "M"):
                        value +=800
                        i+=1
            elif (s[i] == "D"):

                value+=500
            elif (s[i] == "M"):

                value+=1000

            i+=1

        return value