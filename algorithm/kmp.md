如何背诵kmp算法？
记住$\pi$函数定义。最长的，真前缀等于真后缀的长度
记住典型例子：`badbagbadbad`是`000120123453`
- 其中对于`i=11, j=5`时刻（一个指向最后的`d`，一个指向`g`）
- 考察$\pi(4)=2$，而此时$\pi(11)$应当等于3，即`s[11] == s[2]`

因此就记住了核心
```python
while s[i] != s[j] and j != -1:
    j = pi[j-1]
j += 1
pi[i] = j
```

对于在`hello`里找`ll`，可以直接考察`ll#hello`的$\pi$函数。其中`#`为分隔符

- 注意：是真前缀！所以`pi[0]`是0而不是1（否则会导致死循环）