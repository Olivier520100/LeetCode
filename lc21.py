class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        resultlinkedlist = None;
        if (list1 != None or list2 != None):
            resultlinkedlist = ListNode()
        returnlist = resultlinkedlist

        while (list1 != None or list2 != None):
            
            if (list1 != None and list2 != None):
                if (list1.val <= list2.val):
                    returnlist.val = list1.val
                    list1 = list1.next
                else: 
                    returnlist.val = list2.val
                    list2 = list2.next

            elif (list1 != None):

                returnlist.val = list1.val
                list1 = list1.next
            elif (list2 != None):

                returnlist.val = list2.val
                list2 = list2.next
            if (list1 != None or list2 != None):

                returnlist.next = ListNode()
                returnlist = returnlist.next



        return resultlinkedlist