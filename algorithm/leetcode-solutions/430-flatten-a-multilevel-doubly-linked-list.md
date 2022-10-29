- https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# 递归[[oi-wiki-basic/recursion]]，效率较低
```python
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        child = self.flatten(head.child)
        if child:
            child_cur = child
            while(child_cur.next):
                child_cur = child_cur.next
            child_cur.next = head.next
            child.prev = head
            if self.flatten(head.next):
                head.next.prev = child_cur
            head.next = head.child
            head.child = None
            return head
        self.flatten(head.next)
        return head
```