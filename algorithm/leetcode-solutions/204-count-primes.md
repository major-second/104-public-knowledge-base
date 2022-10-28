- https://leetcode.com/problems/count-primes
# 我的提交
```cpp
class Solution {
public:
    int countPrimes(int n) {
        if (n<=2) return 0;
        vector<int> v(n, 1);
        v[0] = 0;
        v[1] = 0;
        int total = 0;
        for (int factor1=2; factor1<n; factor1++){
            if (!v[factor1]) continue;
            total++;
            for (int factor2=factor1; (long)factor2*factor1<n; factor2++) v[factor2*factor1] = 0;
        }
        return total;
    }
};
```
- 总体思想属于[[enumerate]]，不断剪枝
  - 整个埃拉托色尼筛就是不断剪枝，即已经合数了就不用再考察了
  - $ab=n$则至少一个不超过$\sqrt n$
    - 本质是对称性，假设$a<b$
    - 这里体现在`int factor2=factor1;`
- 典型错误：在上面代码中，外层循环到`factor1*factor1<n`就停下了，这时`total`统计不全
  - 显然，如果这样，那最后还要遍历数组加和。总之逃不过$O(n)$
- 注意相乘时可能[[overflow]]