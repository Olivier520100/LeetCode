import numpy as np
import copy

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a=copy.deepcopy(nums)
        b=copy.deepcopy(nums)
        i = 1
        while (i < len(nums)):
            a[i] = a[i-1]+ a[i]
            i+=1
        i = len(b)-2
        while (i > -1):
            b[i] = b[i+1]+ b[i]
            i-=1
        i = 0
        boolea = False
        while (i < len(a) and boolea == False):
            if (a[i]==b[i]):
                boolea = True
            i+=1
        if boolea == False:
            return -1
        else: 
            return i-1
        