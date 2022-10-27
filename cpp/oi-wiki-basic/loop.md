- 前置[[oi-wiki-basic/var]]

https://oiwiki.org/lang/loop/
`while(){}`
`for(;;){}`（特别注意不是逗号）
范围`for`：`for (auto x:s)`，在[[container-intro]]中用到
`break`在`for`循环中也能用，但是是到“更新”（`i++`）那里，而非直接跳出，也就是最后`i`还会加一
- 应用举例：循环同时，连续的重复元素只取一次
https://leetcode-cn.com/problems/4sum/中可能用到
- 原始版本循环
```cpp
for (int i=0;i<n;i++){
    for (int j=i+1;j<n;j++){
    }
}
```
- snippet版：4行一组，原来1行变成现在4行
```cpp
int former_i = INT_MAX; //假设数据里不会出现这么大的数
for (int i=0;i<n;i++){
    if (nums[i] == former_i) continue;
    former_i = nums[i];

    int former_j = INT_MAX; //注意作用域。这个变量不能定义在最外层，想想为什么
    for (int j=i+1;j<n;j++){
        if (nums[j] == former_j) continue;
        former_j = nums[j];
    }
}
```