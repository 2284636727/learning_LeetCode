'''
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:return l2
        if l2 is None:return l1

        h1 = l1
        h2 = l2
        while h1.next is not None or h2.next is not None:
            if h1.next is None:
                h1.next = ListNode(0)
            if h2.next is None:
                h2.next = ListNode(0)

            twosum = h1.val + h2.val
            if twosum > 9:
                h1.next.val += 1
                h1.val = twosum%10
            else:
                h1.val = twosum
            h1 = h1.next
            h2 = h2.next
        else:
            twosum = h1.val + h2.val
            if twosum > 9:
                h1.next = ListNode(1)
                h1.val = twosum%10
            else:
                h1.val = twosum
        return l1

l1 = ListNode(2)
l1_2 = ListNode(4)
l1_3 = ListNode(3)
l2 = ListNode(5)
l2_2 = ListNode(6)
l2_3 = ListNode(4)

l1_2.next = l1_3
l1.next = l1_2

l2_2.next = l2_3
l2.next = l2_2

result = Solution().addTwoNumbers(l1,l2)

while result is not None:
    print(result.val)
    result = result.next

'''
GOD SOULTION
My Example:
d = Solution()
l1 = d.make_list_node([2, 4, 3])
l2 = d.make_list_node([5, 6, 4])
d.print_list_node(l1)
d.print_list_node(l2)
d.print_list_node(d.addTwoNumbers(l1, l2))

Output:
[2, 4, 3, ]
[5, 6, 4, ]
[7, 0, 8, ]
'''


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or (l1.val is 0 and l1.next is None):
            return l2
        elif l2 is None or (l2.val is 0 and l2.next is None):
            return l1

        # let's always return a new list basing on l1, will return root finally
        # thus, no need to create a new link list or list node which will take some time and memory
        root = l1
        add = carrier = 0
        l_cur = None
        while l1 and l2:
            add = l1.val + l2.val + carrier
            # if ... else is much faster
            l1.val, carrier = (add - 10, 1) if add > 9 else (add, 0)
            l_cur = l1
            l1, l2 = l1.next, l2.next

        # In case l2 is longer than l1, to fully utilize the chracter of link list, connect the left l2 to l1
        if l2:
            l_cur.next = l2
        # the tail is going to be changed possibly with None
        possible_tail = l_cur
        l_cur = l_cur.next

        # same logic as before
        while l_cur:
            add = l_cur.val + carrier
            # if ... else is much faster
            l_cur.val, carrier = (add - 10, 1) if add > 9 else (add, 0)

            # the tail is going to be changed possibly with None
            possible_tail = l_cur
            l_cur = l_cur.next
        if carrier:
            # Actually we only create one node if possible
            possible_tail.next = ListNode(1)

        return root

    # self defined function to create link list using Python built-in list
    def make_list_node(self, lst):
        if not lst:
            return None
        l = l_cur = ListNode(lst[0])
        for x in lst[1:]:
            temp_node = ListNode(x)
            l_cur.next = temp_node
            l_cur = temp_node
        return l

    # Print the link node list like Python list style
    def print_list_node(self, l):
        # Use the same style, no need to consider special case like None list
        str_lst = ['[']
        while l:
            str_lst.append(str(l.val) + ', ')
            l = l.next
        if len(str_lst) > 1:
            str_lst[-1] = str_lst[-1].rstrip(', ')
        str_lst.append(']')
        print(''.join(str_lst))






