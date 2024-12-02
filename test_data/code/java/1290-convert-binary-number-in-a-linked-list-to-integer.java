class Solution {
    public int getDecimalValue(ListNode head) {
        ListNode node = head;
        int decimalValue = 0;
        while (node != null) {
            decimalValue = decimalValue * 2 + node.val;
            node = node.next;
        }
        return decimalValue;
    }
}