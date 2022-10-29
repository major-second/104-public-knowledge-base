- https://leetcode.cn/problems/regular-expression-matching
- 前置
  - [[oi-wiki-stl/string]]操作，例如`.size(), .substr()`等
- 参考：[[regex]]，[[4-decision-tree]]
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
- 注意[[oi-wiki-basic/recursion]]中讲到的“使递推关系最简单”
- 参考[[func]]，参考[[4-decision-tree]]思想，“特判直接返回”，减少`else`使用
# [[dp]]解法
```cpp
class Solution {
public:
    bool charIsMatch(char a, char b) {
        return a == b || b == '.';
    }
    bool isMatch(string s, string p) {
        int p_size = p.size();
        int s_size = s.size();
        bool match[p_size+1][s_size+1];

        match[p_size][s_size] = 1; // s[s_size:], p[p_size:] are both empty strings
        for (int j=s_size-1; j>=0; j--){
            match[p_size][j] = 0;
        }

        int i=p_size;
        while (i>0){
            if (i>=1 && p[i-1]=='*'){
                i-=2;
                match[i][s_size] = match[i+2][s_size];
                for (int j=s_size-1; j>=0; j--){
                    match[i][j] = match[i+2][j] || match[i][j+1] && charIsMatch(s[j], p[i]);
                }
            } else {
                i-=1;
                match[i][s_size] = 0;
                for (int j=s_size-1; j>=0; j--){
                    match[i][j] = match[i+1][j+1] && charIsMatch(s[j], p[i]);
                }
            }
        }
        return match[0][0];
    }
};
```
比[[oi-wiki-basic/recursion]]快得多
# 拓展讨论
- 一些[[counter-examples]]
  - 认为必须第一个字符就match
      - 不一定！比如`a`对应`c*a`，`c*`可以是0个c
  - 认为`p`和`s`一定同时为空或不为空才能match
      - 不一定！比如`a`对应`ac*`，那么递归一层，考察空字符串和`c*`
  - 因为有`.`的存在，所以容易找出反例说明：数组`match`中的`1`不一定是连续出现的！
- [[dp]]解法中节省空间：状态压缩！
```cpp
class Solution {
public:
    bool charIsMatch(char a, char b) {
        return a == b || b == '.';
    }
    bool isMatch(string s, string p) {
        int s_size = s.size();
        bool match[s_size+1];
        bool match_next[s_size+1];
        int s_pointer=s_size;
        match[s_pointer] = 1;
        while(s_pointer--) match[s_pointer] = 0;

        int p_pointer = p.size();
        while(p_pointer){
            int s_pointer=s_size;
            if (p[p_pointer-1]=='*') {
                p_pointer-=2;
                match_next[s_pointer] = match[s_pointer];
                while(s_pointer--){
                    match_next[s_pointer] = match[s_pointer] || 
                                            match_next[s_pointer+1] && charIsMatch(s[s_pointer], p[p_pointer]);
                }
            } else {
                p_pointer--;
                match_next[s_pointer] = 0;
                while(s_pointer--){
                    match_next[s_pointer] = match[s_pointer+1] && charIsMatch(s[s_pointer], p[p_pointer]);
                }
            }
            for (int i=0;i<s_size+1;i++) match[i] = match_next[i];
        }

        return match[0];
    }
};
```