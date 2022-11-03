- https://leetcode.cn/problems/gray-code/
```cpp
class Solution {
public:
    vector<int> grayCode(int n) {
        if (n==1) return {0,1};
        vector<int> ans = grayCode(n-1);
        int halfLength = ans.size();
        for (int i=0; i<halfLength; i++) ans.push_back(ans[halfLength-1-i] + halfLength);
        return ans;
    }
};
```
- [[oi-wiki-basic/recursion]]
- 构造[[construction]]答案！只要构造出一个即可