import copy
import numpy as np
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1new = copy.deepcopy(l1)
        l1count = 0
        num1 = ""
        while (l1new != None):
            l1count+=1
            num1 = str(l1new.val) + num1
            l1new = l1new.next
        print(num1)
        l2new = copy.deepcopy(l2)
        l2count = 0
        num2 = ""
        while (l2new != None):
            l2count+=1
            num2 = str(l2new.val) + num2
            l2new = l2new.next
        print(num2)
        result = list(str(int(num1)+int(num2)))
        resultarray = np.zeros([len(result)])
        i = 0 
        while i < len(result):
            resultarray[i] = result[i]
            i+=1
        resultarray = np.flip(resultarray)
        resultlinkedlist = ListNode()
        pointerlinkedlist = resultlinkedlist
        k = len(resultarray)
        i = 0
        while i < k:
            pointerlinkedlist.val = int(resultarray[i])
            if ((i+1)!=k):
                pointerlinkedlist.next = ListNode()
                pointerlinkedlist = pointerlinkedlist.next
            i+=1
        
        return resultlinkedlist
        
        