- https://leetcode.cn/problems/building-boxes
- 注意[[loop]]中break的运用。找到了就break
- 注意[[algorithm/trivial-mistakes]]：[[float]]运算留出一些余地，误差
  - 这里不光是浮点误差，还有$n(n-1)(n-2)$和$n^3$的差别问题
- 注意[[character/var]]的类型转换
  - `1.`表示浮点
  - `(int)`强制转换为`int`
  - `long long`防止溢出[[overflow]]。出现数值提升
  - 实际中`pow`需要`#include <math.h>`
```cpp
class Solution {
public:
    // 1, 1 2, 1 2 3, 1 2 3 4, ...
    // sum_1^... n(n+1)/2
    // 1 -> 1 2 3 4: C_6^3
    long long sumFromGuess(long long guess){
        return (guess) * (guess-1) * (guess-2) / 6;
    }

    int minimumBoxes(int n) {
        long long ans = 0;
        long long guess = (long long)pow(n * 6., 1 / 3.);
        long long lower = -1;
        for (long long g = guess-2; g <= guess+3; g++){
            if (sumFromGuess(g-1) < n && n <= sumFromGuess(g)) {
                lower = g-1;
                break;
            }
        }
        cout<<lower;
        ans += (lower-1)*(lower-2)/2;
        n -= sumFromGuess(lower);
        long long guessInner = (long long)pow(n * 2., 1 / 2.);
        long long lowerInner = guessInner;
        for (long long g = guessInner-2; g <= guessInner+3; g++){
            if ((g-1)*(g-2)/2 < n && n <= g*(g-1)/2){
                lowerInner = g-1;
                break;
            }
        }
        return ans + lowerInner;
    }
};
```