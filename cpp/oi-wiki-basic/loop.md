- 前置[[oi-wiki-basic/var]]

https://oiwiki.org/lang/loop/
`while(){}`
`for(;;){}`（特别注意不是逗号）
范围`for`：`for (auto x:s)`，在[[container-intro]]中用到
`break`在`for`循环中也能用，但是是到“更新”（`i++`）那里，而非直接跳出，也就是最后`i`还会加一
- 拓展举例：循环同时，连续的重复元素只取一次，[[18-4sum]]中可能用到
- 原始版本循环（这里没写反花括号）
```cpp
for (int i=0;i<n;i++){
    for (int j=i+1;j<n;j++){
```
- snippet版：4行一组，原来1行变成现在4行
  - 注意假设`INT_MAX`始终不在`nums`内
  - 注意作用域（思考：`former_j_value`为何不能在更外面一层）
```cpp
int former_i_value = INT_MAX;
for (int i=0;i<n;i++){
    if (nums[i]==former_i_value) continue;
    former_i_value = nums[i];

    int former_j_value = INT_MAX;
    for (int j=i+1;j<n;j++){
        if (nums[j]==former_j_value) continue;
        former_j_value = nums[j];
```