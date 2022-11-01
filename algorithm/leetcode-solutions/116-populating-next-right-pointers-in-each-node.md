- https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/
## [[oi-wiki-basic/recursion]]
- 注意执行次序！
- 递归想要想清楚，必须要知道
  - “该函数运行前条件”是什么
  - “该函数运行后，当作具有的性质”是什么
  - 知道了之后就可以把下层调用递归看作黑箱
```cpp
class Solution {
public:
    Node* connect(Node* root) {
        if (!root) return root;
        if (root->next && root->right) root->right->next = root->next->left;
        if (root->left) {
            root->left->next = connect(root->right);
            connect(root->left);
        }
        return root;
    }
};
```
- 这里对`root`要求条件是如果`root`应该有`next`的话，那就已经连好了
- 递归后的性质是`root`及其所有子孙都连好
## 非递归方法：参考官方题解
- 核心：每一层看作[[linked-list]]，遍历时同时更新下一层，因此不需额外空间