/**
 * Leetcode 138.
 *  
 * A linked list is given such that each node contains 
 * an additional random pointer which could point to any node in the list or null.
 *
 * Return a deep copy of the list. 
 *
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class CopyListWithRandomLink {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) {
            return head;
        }
        
        // Generate copied node and embeded to the exist list
        RandomListNode curr = head;
        while (curr != null) {
            RandomListNode nd = new RandomListNode(curr.label);
            nd.next = curr.next;
            curr.next = nd;
            curr = nd.next;
        }
        
        // Generate Random link in the mixed list
        curr = head;
        while (curr != null) {
            if (curr.random != null) {
                // curr.next is the new curr
                // curr.random is old random. curr.random.next is the new random
                curr.next.random = curr.random.next;
            }
            curr = curr.next.next;
        }
        
        // split the list and recover existing list
        RandomListNode newHead = new RandomListNode(-1);
        RandomListNode newCurr = newHead;
        curr = head;
        while (curr != null) {
            newCurr.next = curr.next;
            newCurr = newCurr.next;
            curr.next = curr.next.next;
            curr = curr.next;
        }
        return newHead.next;
    }
}
