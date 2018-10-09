"""
This is AddTwoNumbers class module
"""


class ListNode(object):
    """
    This is ListNode class
    """

    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f"{self.val}"


class AddTwoNumbers(object):
    """
    This is AddTwoNumbers class
    """

    def add_two_numbers(self, l1: ListNode, l2: ListNode):
        """
        add_two_numbers

        Args:
            l1: ListNode
            l2: ListNode
        Returns:
            node: ListNode
        Raises:
            None
        """
        carry = 0
        dummy = current_node = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            current_node.next = ListNode(val)
            current_node = current_node.next
        return dummy.next
