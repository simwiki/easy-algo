import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_op import LinkedList, ListNode


def bubble_sort(head: LinkedList):
    node_i = head
    tail = None
    while node_i:
        node_j = head
        while node_j and node_j.next != tail:
            if node_j.val > node_j.next.val:
                node_j.val, node_j.next.val = node_j.next.val, node_j.val
            node_j = node_j.next
        tail = node_j
        node_i = node_i.next
    return head


if __name__ == "__main__":
    nums = [5, 3, 1, 9, 7]
    demo = LinkedList(nums=nums)
    print(demo)
    head = bubble_sort(head=demo.head)

    cur = head
    output = []
    while cur:
        output.append(cur.val)
        cur = cur.next
    print("===>".join(map(str,output)))


