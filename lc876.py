class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ResultLinkedList = head
        LinkedPointer1 = ResultLinkedList
        LinkedPointer2 = ResultLinkedList
        i = 0

        while (LinkedPointer2 != None):
            LinkedPointer2 = LinkedPointer2.next
            if (i % 2 == 1):
                LinkedPointer1 = LinkedPointer1.next
            i+=1

        print(LinkedPointer1)
        return LinkedPointer1
    