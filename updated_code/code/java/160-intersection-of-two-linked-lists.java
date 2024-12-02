/**
 * This class provides a solution to find the intersection of two linked lists.
 */
public class Solution {
    /**
     * Returns the node at which the two linked lists intersect.
     * If the two linked lists do not intersect, returns null.
     *
     * @param headA the head of the first linked list
     * @param headB the head of the second linked list
     * @return the node at which the two linked lists intersect
     */
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }

        ListNode pItemA = headA;
        ListNode pItemB = headB;

        while (pItemA != pItemB) {
            pItemA = pItemA != null ? pItemA.next : headB;
            pItemB = pItemB != null ? pItemB.next : headA;
        }

        return pItemA;
    }
}