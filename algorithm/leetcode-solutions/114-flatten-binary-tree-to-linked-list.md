- https://leetcode.com/problems/flatten-binary-tree-to-linked-list
```cpp
class Solution {
public:
    TreeNode* getDeepest(TreeNode* root){
        // root != nullptr;
        while(root->right) root = root->right;
        return root;
    }
    void flatten(TreeNode* root) {
        if (!root) return;
        flatten(root->right);
        flatten(root->left);
        if (root->left) {
            TreeNode* leftDeepest = getDeepest(root->left);
            leftDeepest->right = root->right;
            root->right = root->left;
            root->left = nullptr;
        }
    }
};
```
- [[oi-wiki-basic/recursion]]