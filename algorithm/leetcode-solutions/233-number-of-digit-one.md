- https://leetcode.com/problems/number-of-digit-one
```cpp
class Solution {
public:
    int countDigitOne(int n) {
        long long powerOf10 = 1;
        long long total = 0;
        while(powerOf10 <= n){
            int prefix = n / (powerOf10 * 10);
            switch (n / powerOf10 % 10){
                case 0:
                    total += prefix * powerOf10;
                    break;
                case 1:
                    total += prefix * powerOf10 + n % powerOf10 + 1;
                    break;
                default:
                    total += (prefix+1) * powerOf10;
            }
            powerOf10 *= 10;
        }
        return total;
    }
};
```
- 主体是[[re-classification]]：按每一位出现的1数量计算
- 回忆[[oi-wiki-basic/branch]]，注意`break`
- 注意避免[[overflow]]