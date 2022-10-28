- 算法题中溢出：`long long`或者`unsigned long long`看能不能暴力过一下
  - 反正，看数据范围。可能的“大”数据在四则运算时就可能溢出，可以尝试提升到`long long`（参考[[oi-wiki-basic/var]]）
    - 乘法：[[204-count-primes]]
    - 加减法：[[18-4sum]]
- 求组合数余数的
https://oi-wiki.org/math/number-theory/lucas/#exlucas
扩展卢卡斯定理
当然这个比较复杂。其实只需知道逆元和中国剩余定理就够了
- https://leetcode.cn/problems/reverse-integer/submissions/
比如通过`INT_MAX/10`和当前值比较，判断可不可以`*=10`
注意需要`<limits.h>`
有些语言溢出会报错，无法AC. 所以需要避免溢出的前提下判断。