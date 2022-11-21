- https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal
- [[bfs]]
- [[deque]]，因为需要两个方向
```cpp
class Solution {
public:
    vector<int> nextTier(deque<TreeNode*>& frontiers, bool& currentLeftToRight){
        vector<int> ans;
        int dequeSize = frontiers.size();
        if (currentLeftToRight){
            while(dequeSize--){
                TreeNode* curr = frontiers.back();
                if (curr){
                    ans.push_back(curr->val);
                    frontiers.push_front(curr->left);
                    frontiers.push_front(curr->right);
                }
                frontiers.pop_back();
            }
        } else {
            while(dequeSize--){
                TreeNode* curr = frontiers.front();
                if (curr){
                    ans.push_back(curr->val);
                    frontiers.push_back(curr->right);
                    frontiers.push_back(curr->left);
                }
                frontiers.pop_front();
            }
        }
        currentLeftToRight = !currentLeftToRight;
        return ans;
    }
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        bool currentLeftToRight = true;
        deque<TreeNode*> frontiers {root};
        vector<vector<int>> ans;
        while(1){
            vector<int> next_ans = nextTier(frontiers, currentLeftToRight);
            if (next_ans.empty()) return ans;
            ans.push_back(next_ans);
        }
        return ans;
    }
};
```