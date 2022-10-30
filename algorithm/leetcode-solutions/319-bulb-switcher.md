- https://leetcode.com/problems/bulb-switcher/
# 就是数学题。奇数个因数就是完全平方数
- 注意[[leave-one-out]]！是小于等于$n$都算
```cpp
class Solution {
public:
    int bulbSwitch(int n) {
        return (int)sqrt(n+0.5);
    }
};
```