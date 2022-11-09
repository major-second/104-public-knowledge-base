- https://leetcode.com/problems/reverse-nodes-in-k-group/description/
```cpp
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(k==1) return head;

        ListNode* cur = head;
        for (int i=0; i<k; i++){
            if (!cur) return head;
            cur = cur->next;
        }

        ListNode* alreadyDetached = head;
        ListNode* nextDetach = alreadyDetached->next;
        ListNode* remain = nextDetach->next;
        alreadyDetached->next = nullptr;
        ListNode* tmpTail = alreadyDetached;

        for (int i=1; i<k; i++){
            nextDetach->next = alreadyDetached;
            alreadyDetached = nextDetach;
            nextDetach = remain;
            if (!remain) return alreadyDetached;
            remain = remain->next;
        }
        tmpTail->next = reverseKGroup(nextDetach, k);
        return alreadyDetached;
    }
};
```
- [[linked-list]]
- [[oi-wiki-basic/simulate]]题目