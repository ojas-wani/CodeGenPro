from typing import Optional
from ListNode import ListNode

class Solution:
    """
    This class is used to solve the problem of deleting duplicates from a sorted linked list.
    """
    def __init__(self):
        """
        Constructor of the Solution class.
        """
        pass

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        This function is used to delete duplicates from a sorted linked list.
        
        Parameters:
        head (Optional[ListNode]): The head of the linked list.
        
        Returns:
        Optional[ListNode]: The head of the linked list after duplicates are removed.
        """
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            if current.next.val == current.next.next.val:
                val = current.next.val
                while current.next and current.next.val == val:
                    current.next = current.next.next
            else:
                current = current.next
        return dummy.next