- https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
```cpp
class Solution {
public:
    vector<int> getPi(const string& p){
        // badbagbadbad: -10000120123453
        int length = p.size();
        vector<int> pi {-1};
        
        int comparedTo = -1;
        for (int cur = 1; cur<=length; cur++){
            while (comparedTo>=0 && p[cur-1]!=p[comparedTo]){
                comparedTo = pi[comparedTo];
            }
            pi.push_back(++comparedTo);
        }
        return pi;
    }
    
    int strStr(string haystack, string needle) {
        auto pi = getPi(needle+'#'+haystack);
        int n = needle.size();
        for (int i=0;i<pi.size();i++) if (pi[i]==n) return i - 2 * n - 1;
        return -1;
    }
};
```
- 解说参见[[kmp]]
- 本实现当然有时间浪费。没有必要走完整个字符串！