- https://leetcode.cn/problems/regular-expression-matching
- 基本思想就是“特判直接返回”
```cpp
class Solution {
public:

    bool matchChar(char a, char b){
        return a==b || b=='.';
    }
    bool isMatch(string s, string p) {
        int np = p.size();
        int ns = s.size();
        if (!np) return !ns;

        bool hard = np==1 || p[1]!='*';

        if (hard) {
            if (!ns) return false;
            if (not matchChar(s[0],p[0])) return false;
            return isMatch(s.substr(1,ns-1),p.substr(1,np-1));
        }

        char p_first = p[0];
        p = p.substr(2,np-2);
        if (isMatch(s,p)) return true;
        while(!s.empty()){
            if (not matchChar(s[0],p_first)) return false;
            s = s.substr(1,ns);
            if (isMatch(s,p)) return true;
        }
        return false;
    }
};
```
注：最佳方法参见[[dp]]