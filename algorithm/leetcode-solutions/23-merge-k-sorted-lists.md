- 前置[[21-merge-two-sorted-lists]]
- 注意特判[[algorithm/special-case]]：0或1个链表
- https://leetcode.com/problems/merge-k-sorted-lists/
# 分治法[[divide-and-conquer]]，[[oi-wiki-basic/recursion]]
```cpp
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (!list1) return list2;
        if (!list2) return list1;
        
        ListNode* head = nullptr;
        ListNode* cur = nullptr;
        
        ListNode* curPointerArray[2] = {list1, list2};
        while (curPointerArray[0] && curPointerArray[1]){
            int lessIndex = curPointerArray[0]->val > curPointerArray[1]->val; // 0: list1 head is less; 1: list2 head is less.
            ListNode* lessCur = curPointerArray[lessIndex];
            if (cur) cur->next = lessCur;
            if (!cur) head = lessCur;
            cur = lessCur;
            curPointerArray[lessIndex] = lessCur->next;
        }
        
        cur->next = curPointerArray[!curPointerArray[0]];
        return head;
    }
    
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int length = lists.size();
        if (length == 0) return nullptr;
        if (length == 1) return lists[0];
        int mid = length / 2;
        
        auto beginIt = lists.begin();
        vector<ListNode*> listsPart1(beginIt, beginIt + mid);
        vector<ListNode*> listsPart2(beginIt + mid, beginIt + length);
        
        return mergeTwoLists(mergeKLists(listsPart1), mergeKLists(listsPart2)); 
    }
```
- 对分治的分析
  - 出口[[algorithm/special-case]]：0或1个链表
  - 分解：直接分成两个链表组成的vector，参考[[sequence]]中使用两个迭代器初始化
  - 这里的“各自解决”和“归并”非常简单，放到了`return`里一行搞定