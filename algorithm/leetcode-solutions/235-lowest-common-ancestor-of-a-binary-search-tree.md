- https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (p->val > q->val) {
            TreeNode* t = p;
            p = q;
            q = t;
        }
        if (p->val == root->val || q->val == root->val) return root;
        if (p->val < root->val && root->val < q->val) return root;
        if (q->val < root->val) return lowestCommonAncestor(root->left, p, q);
        return lowestCommonAncestor(root->right, p, q);
    }
};
```
- 一来，利用[[symmetry#轮换]]，交换，可[[reduction]]