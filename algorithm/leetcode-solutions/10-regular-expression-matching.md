- https://leetcode.cn/problems/regular-expression-matching
- 必须反复使用“特判直接返回”，参考[[func]]，减少`else`使用
- 参考资料：[[regex]]
# [[oi-wiki-basic/recursion]]递归解法
```cpp
class Solution {
public:
    bool charIsMatch(char a, char b) {
        return a == b || b == '.';
    }
    bool isMatch(string s, string p) {
        int p_size = p.size();
        int s_size = s.size();
        if (p_size==0) return s_size==0;
        bool matchFirst = s_size>0 && charIsMatch(s[0], p[0]);
        if (p_size==1 or p[1]!='*') return matchFirst && isMatch(s.substr(1, s_size-1), p.substr(1, p_size-1));
        if (isMatch(s, p.substr(2, p_size-2))) return true;
        if (!matchFirst) return false;
        return isMatch(s.substr(1, s_size-1), p);
    }
};
```
- `p`是`a*a`这种时，不能让`a*`消耗全部`s`中`a`，也就是不能[[greedy]]，需要[[dp]]
- 注意`if (p_size==0) return s_size==0;`是[[oi-wiki-basic/recursion]]出口