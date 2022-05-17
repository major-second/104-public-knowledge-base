- `long long`或者`unsigned long long`看能不能暴力过一下
- 求组合数余数的
https://oi-wiki.org/math/number-theory/lucas/#exlucas
扩展卢卡斯定理
当然这个比较复杂。其实只需知道逆元和中国剩余定理就够了
- https://leetcode-cn.com/problems/reverse-integer/submissions/
比如通过`INT_MAX/10`和当前值比较，判断可不可以`*=10`
注意需要`<limits.h>`
有些语言溢出会报错，无法AC. 所以需要避免溢出的前提下判断。