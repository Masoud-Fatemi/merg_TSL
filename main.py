"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Initialize a dummy node to facilitate the merge process
        dummy = ListNode()
        current = dummy

        # Traverse through both lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If either of the lists reaches the end, connect the rest of the other list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next  # Return the merged list, excluding the dummy node

"""
In this method, a dummy node is used to simplify the merge process. This dummy node is a placeholder to the start of the merged list. We then iterate through list1 and list2, comparing their node values. The node with the smaller value is appended to the merged list, and we move to the next node in that list. When one of the lists is fully traversed, we simply append the remaining part of the other list to the merged list.

Finally, the method returns the next node of dummy, which is the

head of the merged list. The dummy node itself is not part of the final merged list; it's just a placeholder to help with the merging process.
"""