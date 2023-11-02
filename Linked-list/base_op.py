# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next: ListNode = next
    def __repr__(self):
        return f"{str(self.val)}===>{str(self.next.val if self.next else None)}"

class LinkedList:
    def __init__(self, nums) -> None:
        self.head = None
        self.create(nums)
    
    def create(self, nums):
        if not nums:
            return
        self.head = ListNode(nums[0])
        cur = self.head
        for i in range(1, len(nums)):
            node = ListNode(nums[i])
            cur.next = node
            cur = cur.next
        
    def __repr__(self) -> str:
        cur = self.head
        output = []
        while cur:
            output.append(cur.val)
            cur = cur.next
        return "===>".join(map(str,output))

    @property
    def length(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def find(self, val):
        cur = self.head
        while cur:
            if cur.val == val:
                return cur
            cur = cur.next
        return None

    def insert_front(self, val):
        ...
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def insert_rear(self, val):
        cur = self.head
        while cur.next:
            cur = cur.next
        node = ListNode(val)
        cur.next = node

    def insert_inside(self, index, val):
        # 在第i个节点之后insert新的节点
        cur = self.head
        count = 0
        while cur and count < index:
            count += 1
            cur = cur.next
        node = ListNode(val)
        node.next = cur.next
        cur.next = node

    def change(self, index, val):
        cur = self.head
        count = 0
        while cur and count < index:
            count += 1
            cur = cur.next
        cur.val = val

    def remove_front(self):
        if self.head:
            self.head = self.head.next
    
    def remove_inside(self, index):
        # 删除第i个节点
        cur = self.head
        count = 0
        while cur and  count < index - 1:
            count += 1
            cur = cur.next
        cur.next = cur.next.next

    def remove_rear(self):
        if not self.head.next:
            return
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9]
    demo = LinkedList(nums=nums)
    print(demo)
    print(demo.length)

    print("增")
    demo.insert_front(22)
    print(demo)

    demo.insert_rear(666)
    print(demo)

    demo.insert_inside(3, 8888)
    print(demo)

    print("删")
    demo.remove_front()
    print(demo)
    demo.remove_rear()
    print(demo)
    demo.remove_inside(3)
    print(demo)

    print("改")
    demo.change(4, 99)
    print(demo)

    print("查")
    print(demo.find(3))
