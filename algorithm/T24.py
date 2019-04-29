from algorithm.ListNode import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        t_head = ListNode(0)
        t_head.next = head
        p = t_head
        while True:
            if p is None or p.next is None or p.next.next is None:
                break
            print('swap', p.next.val, 'and', p.next.next.val)
            temp1 = p.next
            temp2 = p.next.next.next
            p.next = p.next.next
            p.next.next = temp1
            temp1.next = temp2
            p = p.next.next
        return t_head.next


h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h = Solution().swapPairs(h)
while h is not None:
    print(h.val)
    h = h.next