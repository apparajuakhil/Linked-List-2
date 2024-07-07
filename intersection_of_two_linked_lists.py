"""
Linked-List-2
Problem4 (https://leetcode.com/problems/intersection-of-two-linked-lists/)

Time Complexity : O(m+n)
Space Complexity : O(1)
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

Your code here along with comments explaining your approach:
Trick is to undestand that we need to find intersection inbetween the lists so we calculate each of its lengths and whichever
is longest we need to move its head until both lengths are equal. Once both lengths are equal we traverse both of them parallely
and return any one of head which will result in intersection if there is any else None if reaches end of the list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        lenA = 0
        curr = headA
        while curr is not None:
            curr = curr.next
            lenA += 1

        lenB = 0
        curr = headB
        while curr is not None:
            curr = curr.next
            lenB += 1

        while lenA > lenB:
            headA = headA.next
            lenA -= 1
            
        while lenB > lenA:
            headB = headB.next
            lenB -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA