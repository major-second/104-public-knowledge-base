- 最长回文子串，错误认为
    - 右边新加入的一位“上位”有两种可能：自己上位或是和之前的联合上位。
    - 自己上位：`bccc`，新加入`c`，必须连续一堆重复
    - 联合上位：`bccc`，新加入`b`
    - 分类讨论即可
其实有反例：`bananas`
- https://leetcode.cn/problems/number-of-ways-to-select-buildings/
错误认为：对于`00111001`写成`2321`，然后`2*3*2+3*2*1`这种即可
反例：`01010`
- https://leetcode.cn/problems/remove-duplicate-letters/
错误认为：对于`cacdca`这类，每次看`c`下一位，从左到右看，第一个`cd`，那就留住这个`c`即可
你如果只删除`c`，那么这样确实可以得到字典序最小。比如`acda`
但你要考虑其它字母也会被删。比如`cdacbd`，只看`c`的话当然是`cdaba`好，但是同时考虑`d`的话，应该得到`acbd`更好
# 思维盲区
- [[10-regular-expression-matching]]中很多反例
- [[679-24-game]]
  - 错误认为一定是1+3型。可能是2+2型，如$(9-1)*(1+2)=24$