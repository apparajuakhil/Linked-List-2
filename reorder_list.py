"""
Linked-List-2
Problem2 (https://leetcode.com/problems/reorder-list/)

Time Complexity : O(n)
Space Complexity : O(1)
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

Your code here along with comments explaining your approach:
Trick is to find middle of LL and then reverse the 2nd half of the LL and merge 1 & 2 alternatively

"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if head is None:
            return None

        # 1. Find middle of the LL
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half of the LL
        reversed_head = self.reverse(slow.next)
        slow.next = None

        # 3. Merge 2 halves together
        slow = head
        while reversed_head is not None:
            temp = slow.next
            slow.next = reversed_head
            temp1 = reversed_head.next
            slow.next.next = temp
            slow = temp
            reversed_head = temp1

        # # Alternate 3. Merge 2 halves together
        # p1 = head
        # p2 = reversed_head

        # while p2:
        #     temp1 = p1.next
        #     temp2 = p2.next

        #     p1.next = p2
        #     p2.next = temp1

        #     p1 = temp1
        #     p2 = temp2

        return head

        

    def reverse(self, head):
        if head is None or head.next is None:
            return head

        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev