Python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    A solution to detect a cycle in a linked list.
    
    Args:
    head (ListNode): The head of the linked list.
    
    Returns:
    bool: True if there is a cycle, False otherwise.
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detect a cycle in a linked list.
        
        Args:
        head (ListNode): The head of the linked list.
        
        Returns:
        bool: True if there is a cycle, False otherwise.
        """
        if head is None:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            
            slow = slow.next
            fast = fast.next.next
        
        return True