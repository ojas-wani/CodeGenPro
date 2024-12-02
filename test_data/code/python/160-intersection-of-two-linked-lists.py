class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        pA = headA
        pB = headB

        while pA is not pB:
            if pA is not None:
                pA = pA.next
            else:
                pA = headB

            if pB is not None:
                pB = pB.next
            else:
                pB = headA

        return pA