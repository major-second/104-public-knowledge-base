- https://leetcode.cn/problems/permutation-sequence/
```cpp
class Solution {
public:
    string getPermutationForString(int n, string s, int k, const int* fac){
        int length = s.size();
        if (length==1) return s;
        int base = fac[length-1];
        int part = k / base;
        return s[part] + getPermutationForString(n-1, s.substr(0, part) + s.substr(part+1, length-part-1), k - base*part, fac);
    }
    string getPermutation(int n, int k) {
        int factorial[10];
        factorial[1] = 1;
        for (int i=2; i<=9; i++) factorial[i] = factorial[i-1] * i;

        string s;
        for (int i=1; i<=n; i++) s.push_back('0' + i);
        return getPermutationForString(n, s, k-1, factorial);
    }
};
```
- 注意`'0'+i`，不要直接`push_back(i)`
- [[oi-wiki-basic/recursion]]