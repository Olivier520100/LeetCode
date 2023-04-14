class Solution:

    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a =[]
        while (head != None):
            a.append(head.val)
            head = head.next
        i = len(a)-1
        resultlinkedlist = None
        if (i > -1):
            resultlinkedlist = ListNode()
            pointerlinkedlist = resultlinkedlist

        while (i > -1):
            pointerlinkedlist.val = a[i]
            i-=1
            if (i > -1):
                pointerlinkedlist.next = ListNode()
                pointerlinkedlist = pointerlinkedlist.next

        return resultlinkedlist
            
            
            

