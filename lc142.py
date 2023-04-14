# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        loopdetect = False
        currentnum = 0 
        hashtable = {"":""}
        while (loopdetect == False and head != None):
            hashval = hash(head)
            if (str(hashval) in hashtable):
                loopdetect = True
            else:
                hashtable.update({str(hashval):str(currentnum)})
                head = head.next   

            currentnum +=1
        if loopdetect == False:
            return None
        else: 
            return head
