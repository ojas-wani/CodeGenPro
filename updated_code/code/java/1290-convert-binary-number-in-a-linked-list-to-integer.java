/**
 * This solution assumes that the linked list does not contain leading zeros.
 * It converts the binary representation stored in the linked list to a decimal value.
 *
 * @author <your-name>
 */
package com.your-company;

import java.util.List;
import java.util.scanner;

public class Solution {
    public int getDecimalValue(ListNode head) {
        // Construct a StringBuilder to store the binary representation
        StringBuilder binaryRepresentation = new StringBuilder();

        // Traverse the linked list and append the value of each node to the binary representation
        ListNode node = head;
        while (node != null) {
            binaryRepresentation.append(node.val);
            node = node.next;
        }

        // Convert the binary representation to a decimal value
        int decimalValue = Integer.parseInt(binaryRepresentation.toString(), 2);

        return decimalValue;
    }
}