- 前置[[pointer]]
- https://leetcode.cn/problems/merge-two-sorted-lists
# 第一版解答
```cpp
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (!list1) return list2;
        if (!list2) return list1;
        
        ListNode* head = nullptr;
        ListNode* cur = nullptr;
        
        ListNode* cur1 = list1;
        ListNode* cur2 = list2;
        while (cur1 && cur2){
            if (cur1->val <= cur2->val){
                if (cur) cur->next = cur1;
                if (!cur) head = cur1;
                cur = cur1;
                cur1 = cur1->next;
            } else {
                if (cur) cur->next = cur2;
                if (!cur) head = cur2;
                cur = cur2;
                cur2 = cur2->next;
            }
        }
        
        if (!cur1) cur->next = cur2;
        if (!cur2) cur->next = cur1;
        return head;
    }
};
```
- 其实有点与其说是算法题更像在[[oi-wiki-basic/simulate]]
  - 故一定要在草稿纸上先画图
- 特判[[special-case]]：`list1, list2`中有`nullptr`
- 出现了结束时额外处理，参考[[loop]]
# 利用对称性，减少重复代码
- 参考[[1-clean-code]]
```cpp
class Solution {
public:
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
};
```
# 合理合并[[special-case]]，减少代码量
- 这里是[[化归]]思想，多增加一个链表头，统一情况
```cpp
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* head = new ListNode(0);
        ListNode* cur = head;
        ListNode* curPointerArray[2] = {list1, list2};
        while (curPointerArray[0] && curPointerArray[1]){
            int lessIndex = curPointerArray[0]->val > curPointerArray[1]->val; // 0: list1 head is less; 1: list2 head is less.
            ListNode* lessCur = curPointerArray[lessIndex];
            if (!head->next) head->next = lessCur;
            cur->next = lessCur;
            cur = lessCur;
            curPointerArray[lessIndex] = lessCur->next;
        }
        
        cur->next = curPointerArray[!curPointerArray[0]];
        return head->next;
    }
};
```